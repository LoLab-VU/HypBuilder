
from collections import defaultdict
from csv import reader as rd
import numpy as np
from copy import deepcopy
from itertools import product
from pysb.builder import Builder
import re
from pysb.core import MonomerPattern, ComplexPattern, RuleExpression, ReactionPattern, ANY, WILD
from numpy.random import choice
from pysb.export.pysb_flat import PysbFlatExporter
import os
from pysb.bng import generate_equations
import shutil
# from pyvipr.pysb_viz.static_viz import PysbStaticViz


class Node:

    def __init__(self):
        self.labels = []
        self.initial = []
        self.reactions = []
        self.optional_reactions = []
        self.fill_binding = []
        self.objective = False


class Reaction:

    def __init__(self, molecule, templates, observables, expressions):
        self.molecule = molecule
        self.templates = templates
        self.observables = observables
        self.expressions = expressions
        self.parsed_templates = []


class Model:

    def __init__(self):
        self.name = None
        self.library = defaultdict(dict)
        self.text_library = defaultdict(list)
        self.nodes = {}
        self.iv_priorities = defaultdict(list)
        self.required_reactions = []
        self.optional_reactions = []
        self.listed_reactions = []
        self.lists = []
        self.text_top = []
        self.text_bottom = []
        self.text_obs = []
        self.rules = []


class ModelAssembler:

    def __init__(self, library, model_description, obs='monomers', network_figs=False):
        self.base_model = Model()
        self.import_library(library)
        self.import_labels(model_description)
        self.obs = obs
        self.network_figs = network_figs
        self.models = []
        self.enumerate_models()
        self.enumerate_initial_value_combinations()
        self.build_models()

    def import_library(self, file_name):

        molecule = None
        reaction = None
        templates = []
        observables = []
        expressions = []
        text = []
        text_read = False
        SSS = False

        library_file = open(file_name)
        for line in library_file:
            if text_read and '+++' in line:
                text_read = False
                self.base_model.text_library[text[0]] = text[1:]
                text = []
            if text_read:
                text.append(line)
            if 'text' in line:
                text.append(line[6:-1])
                text_read = True
            if 'molecule:' in line:
                SSS = False
                molecule = line.split(':', 1)[1].strip()
            if 'reaction:' in line:
                reaction = line.split(':', 1)[1].strip()
            if 'template:' in line:
                templates.append(line.split(':', 1)[1].strip())
            if 'observable' in line:
                observables.append(line.split(':', 1)[1].strip())
            if 'expression' in line:
                expressions.append(line.split(':', 1)[1].strip())
            if '+++' in line and not SSS:
                self.base_model.library[molecule][reaction] = \
                    Reaction(molecule, templates, observables, expressions)
            if '$$$' in line:
                SSS = True
                self.base_model.library[molecule][reaction] = \
                    Reaction(molecule, templates, observables, expressions)
                reaction = None
                templates = []
                observables = []
                expressions = []

    def import_labels(self, file_name):

        self.base_model.name = file_name.split('.')[0]
        components = False
        labels = False
        required = False
        optional = False
        listed = False
        lists = False
        fill_binding = False
        text_top = False
        text_bottom = False
        text_obs = False
        rules = False

        with open(file_name) as label_file:

            # read in csv file
            reader = rd(label_file)
            label_list = list(reader)

            for i, each in enumerate(label_list):
                if each:
                    for j, item in enumerate(each[:-1]):

                        if each[j].strip()[0] == '{' and each[j+1].strip()[-1] == '}':
                            label_list[i][j] = label_list[i][j] + ',' + label_list[i][j+1]
                            label_list[i].pop(j+1)
                            break

            for i, each in enumerate(label_list):
                if each:
                    if each[0][0] == '#':
                        continue
                    if each[0][0] == '$':
                        break
                    if each[0].strip() == 'model components':
                        components = True
                        labels = False
                        required = False
                        optional = False
                        listed = False
                        lists = False
                        competition = False
                        fill_binding = False
                        text_top = False
                        text_bottom = False
                        text_obs = False
                        rules = False
                        continue
                    if each[0].strip() == 'labels':
                        components = False
                        labels = True
                        required = False
                        optional = False
                        listed = False
                        lists = False
                        competition = False
                        fill_binding = False
                        text_top = False
                        text_bottom = False
                        text_obs = False
                        rules = False
                        continue
                    if each[0].strip() == 'required reactions':
                        components = False
                        labels = False
                        required = True
                        optional = False
                        listed = False
                        lists = False
                        competition = False
                        fill_binding = False
                        text_top = False
                        text_bottom = False
                        text_obs = False
                        rules = False
                        continue
                    if each[0].strip() == 'optional reactions':
                        components = False
                        labels = False
                        required = False
                        optional = True
                        listed = False
                        lists = False
                        competition = False
                        fill_binding = False
                        text_top = False
                        text_bottom = False
                        text_obs = False
                        rules = False
                        continue
                    if each[0].strip() == 'listed reactions':
                        components = False
                        labels = False
                        required = False
                        optional = False
                        listed = True
                        lists = False
                        competition = False
                        fill_binding = False
                        text_top = False
                        text_bottom = False
                        text_obs = False
                        rules = False
                        continue
                    if each[0].strip() == 'lists':
                        components = False
                        labels = False
                        required = False
                        optional = False
                        listed = False
                        lists = True
                        competition = False
                        fill_binding = False
                        text_top = False
                        text_bottom = False
                        text_obs = False
                        rules = False
                        continue
                    if each[0].strip() == 'competitive binding':
                        components = False
                        labels = False
                        required = False
                        optional = False
                        listed = False
                        lists = False
                        competition = True
                        fill_binding = False
                        text_top = False
                        text_bottom = False
                        text_obs = False
                        rules = False
                        continue
                    if each[0].strip() == 'fill binding':
                        components = False
                        labels = False
                        required = False
                        optional = False
                        listed = False
                        lists = False
                        competition = False
                        fill_binding = True
                        text_top = False
                        text_bottom = False
                        text_obs = False
                        rules = False
                        continue
                    if each[0].strip() == 'text top':
                        components = False
                        labels = False
                        required = False
                        optional = False
                        listed = False
                        lists = False
                        competition = False
                        fill_binding = False
                        text_top = True
                        text_bottom = False
                        text_obs = False
                        rules = False
                        continue
                    if each[0].strip() == 'text bottom':
                        components = False
                        labels = False
                        required = False
                        optional = False
                        listed = False
                        lists = False
                        competition = False
                        fill_binding = False
                        text_top = False
                        text_bottom = True
                        text_obs = False
                        rules = False
                        continue
                    if each[0].strip() == 'text obs':
                        components = False
                        labels = False
                        required = False
                        optional = False
                        listed = False
                        lists = False
                        competition = False
                        fill_binding = False
                        text_top = False
                        text_bottom = False
                        text_obs = True
                        rules = False
                        continue
                    if each[0].strip() == 'Boolean rules':
                        components = False
                        labels = False
                        required = False
                        optional = False
                        listed = False
                        lists = False
                        competition = False
                        fill_binding = False
                        text_top = False
                        text_bottom = False
                        text_obs = False
                        rules = True
                        continue

                    if components:

                        # initialize nodes
                        node = each[0].strip()
                        self.base_model.nodes[node] = Node()

                        # find data nodes and iv's
                        values = []
                        for item in each[1:]:
                            if '{' in item:
                                item = item.strip()[1:-1].split('|')
                                for every in item:
                                    if every.strip() == 'd':
                                        self.base_model.data_nodes.append(each[0].strip())
                                    if every.strip().split(':')[0] == 'path':
                                        self.base_model.paths[every.strip().split(':')[1]].append(each[0].strip())
                                    if every.strip().split(':')[0] == 'priority':
                                        self.base_model.iv_priorities[each[0].strip()].append(every.strip().split(':')[1:])
                            else:
                                values.append(item)

                        # list_of_ranges = []
                        values = [x.strip() for x in values]
                        for item in values:
                            if ':' not in item:
                                self.base_model.nodes[node].initial.append(item.strip())
                            else:
                                item = item.split(':')
                                # based on desired number of I.V.'s
                                # example: 3:4-6 -> ['4.0', '5.0', '6.0']
                                if '-' in item[1]:
                                    num, param_range = float(item[0]), item[1]
                                    param_range = param_range.split('-')
                                    start, stop = float(param_range[0]), float(param_range[1])
                                    self.base_model.nodes[node].initial.extend(
                                        list(np.arange(start, stop, (stop - start) / (num-1))))
                                    for j, every in enumerate(self.base_model.nodes[node].initial):
                                        self.base_model.nodes[node].initial[j] = str(every)
                                    self.base_model.nodes[node].initial.append(str(stop))
                                # based on desired increment
                                # example: 4-6:1 -> ['4.0', '5.0', '6.0']
                                if '-' in item[0]:
                                    param_range, inc = item[0], float(item[1])
                                    param_range = param_range.split('-')
                                    start, stop = float(param_range[0]), float(param_range[1])
                                    self.base_model.nodes[node].initial.extend(list(np.arange(start, stop, inc)))
                                    if stop - self.base_model.nodes[node].initial[-1] == inc:
                                        self.base_model.nodes[node].initial.append(stop)
                                    for j, every in enumerate(self.base_model.nodes[node].initial):
                                        self.base_model.nodes[node].initial[j] = str(every)

                    if labels:  # DON'T BELIEVE THIS IS USED ANY LONGER
                        for lab in each[1:]:
                            if lab.strip() not in self.base_model.library:
                                print('%s not in library', lab)
                                quit()
                            else:
                                self.base_model.nodes[each[0].strip()].labels.append(lab.strip())

                    if required:
                        each = [x.strip() for x in each]
                        self.base_model.required_reactions.append(deepcopy(each))
                        for item in each[1:]:
                            if '(' in item and '{' not in item:
                                item = item.split('(')
                                item[1] = item[1].split('[')[1][:-1]
                                if item[1] not in self.base_model.library:
                                    print('"' + item[1] + '" not in library')
                                    quit()
                                if item[0] not in self.base_model.nodes:
                                    print('"' + item[0] + '" not in molecule list')
                                    quit()
                                # labels are probably not necessary at the moment
                                # but could be relevant later
                                if item[1] not in self.base_model.nodes[item[0]].labels:
                                    self.base_model.nodes[item[0]].labels.append(item[1])

                    if optional:
                        each = [x.strip() for x in each]
                        self.base_model.optional_reactions.append(deepcopy(each))
                        for item in each[1:]:
                            if '(' in item and '{' not in item:
                                item = item.split('(')
                                item[1] = item[1].split('[')[1][:-1]
                                if item[1] not in self.base_model.library:
                                    print('"' + item[1] + '" not in library')
                                    quit()
                                if item[0] not in self.base_model.nodes:
                                    print('"' + item[0] + '" not in molecule list')
                                    quit()
                                # labels are probably not necessary at the moment
                                # but could be relevant later
                                if item[1] not in self.base_model.nodes[item[0]].labels:
                                    self.base_model.nodes[item[0]].labels.append(item[1])

                    if listed:
                        each = [x.strip() for x in each]
                        self.base_model.listed_reactions.append(deepcopy(each))
                        for item in each[1:]:
                            if '(' in item and '{' not in item:
                                item = item.split('(')
                                item[1] = item[1].split('[')[1][:-1]
                                if item[1] not in self.base_model.library:
                                    print('"' + item[1] + '" not in library')
                                    quit()
                                if item[0] not in self.base_model.nodes:
                                    print('"' + item[0] + '" not in molecule list')
                                    quit()
                                # labels are probably not necessary at the moment
                                # but could be relevant later
                                if item[1] not in self.base_model.nodes[item[0]].labels:
                                    self.base_model.nodes[item[0]].labels.append(item[1])

                    if lists:
                        each = [x.strip() for x in each]
                        self.base_model.lists.append(deepcopy(each))

                    if fill_binding:
                        self.base_model.nodes[each[0].strip()].fill_binding.append(
                            [each[2].strip(), each[1].strip(), each[3].strip(), each[4].strip()])

                    if text_top:
                        self.base_model.text_top.append(''.join(each))

                    if text_bottom:
                        self.base_model.text_bottom.append(''.join(each))

                    if text_obs:
                        self.base_model.text_obs.append(''.join(each))

                    if rules:
                        self.base_model.rules.append(each[0].split(':')[1].strip())

    def bin_tree(self, nodes, accepted, reaction_list, TTs):

        nodesT = deepcopy(nodes)
        nodesT.append(True)
        nodesF = deepcopy(nodes)
        nodesF.append(False)

        continueTrue = True
        continueFalse = True

        for each in TTs:
            maxTTnode = 0
            for item in TTs[each][0][:-1]:
                if int(item) > int(maxTTnode):
                    maxTTnode = item

            if int(maxTTnode) <= len(nodesT):

                Tvector = []
                for item in TTs[each][0][:-1]:
                    Tvector.append(nodesT[int(item)-1])

                for item in TTs[each][1:]:
                    if Tvector == item[:-1] and not item[-1]:
                        continueTrue = False
                        break
            if not continueTrue:
                break

        for each in TTs:
            maxTTnode = 0
            for item in TTs[each][0][:-1]:
                if int(item) > int(maxTTnode):
                    maxTTnode = item

            if int(maxTTnode) <= len(nodesF):

                Fvector = []
                for item in TTs[each][0][:-1]:
                    Fvector.append(nodesF[int(item) - 1])

                for item in TTs[each][1:]:
                    if Fvector == item[:-1] and not item[-1]:
                        continueFalse = False
                        break
            if not continueFalse:
                break

        if len(nodesT) < len(reaction_list) and continueTrue:
            self.bin_tree(nodesT, accepted, reaction_list, TTs)

        if len(nodesF) < len(reaction_list) and continueFalse:
            self.bin_tree(nodesF, accepted, reaction_list, TTs)

        if len(nodesT) == len(reaction_list) and continueTrue:
            accepted.append(nodesT)

        if len(nodesF) == len(reaction_list) and continueFalse:
            accepted.append(nodesF)

    def enumerate_models(self):

        # listed reactions
        reaction_numbers = defaultdict(list)
        for each in self.base_model.listed_reactions:
            if each:
                for item in each:
                    if '{' in item:
                        item = item[1:-1].split('|')
                        for every in item:
                            if ':' in every and every.split(':')[0].strip() == 'list':
                                reaction_numbers[every.split(':')[1].strip()] = each

        lists_of_rxns = []
        for each in self.base_model.lists:
            lists_of_rxns.append([])
            for item in each[1:]:
                lists_of_rxns[-1].append(reaction_numbers[item])
        if not lists_of_rxns:
            lists_of_rxns.append([])

        rxns_list = []
        reactions_dict = defaultdict(list)
        for i, each in enumerate(self.base_model.optional_reactions):
            rxns_list.append(each[0])
            reactions_dict[each[0]] = each[1:]

        Bools = []
        for each in self.base_model.rules:
            each = each.replace('not', ' not ')
            each = each.replace('and', ' and ')
            each = each.replace('or', ' or ')
            each = each.replace('(', ' ( ')
            each = each.replace(')', ' ) ')
            Bools.append(each.split())

        BoolSpecies2 = defaultdict(list)
        for i, each in enumerate(Bools):
            for item in each:
                if item.isdigit() and item not in BoolSpecies2[i]:
                    BoolSpecies2[i].append(item)

        TF2 = defaultdict(list)
        for each in BoolSpecies2:
            TF2[each] = list(product(['True', 'False'], repeat=len(BoolSpecies2[each])))

        TFtable2 = defaultdict(list)
        for i, each in enumerate(Bools):
            BoolSpecies2[i].append('value')
            TFtable2[i].append(BoolSpecies2[i])

            for item in TF2[i]:
                express = deepcopy(each)
                for j, every in enumerate(express):
                    if every.isdigit():
                        express[j] = item[BoolSpecies2[i].index(every)]
                item = list(item)
                item.append(eval(' '.join(express)))
                TFtable2[i].append(item)

        for i, each in enumerate(TFtable2):
            for j, item in enumerate(TFtable2[each]):
                for k, every in enumerate(item):
                    if every == 'True':
                        TFtable2[i][j][k] = True
                    if every == 'False':
                        TFtable2[i][j][k] = False

        rxns = []
        accepted_rxn_sets = []
        self.bin_tree(rxns, accepted_rxn_sets, rxns_list, TFtable2)

        rxnComboList = [[]]
        for each in accepted_rxn_sets:
            comboList = []
            for j, item in enumerate(each):
                if item:
                    comboList.append(j)
            if comboList:
                rxnComboList.append(comboList)

        for j, each in enumerate(rxnComboList):
            for k, item in enumerate(each):
                rxnComboList[j][k] = self.base_model.optional_reactions[item][1:]

        for j, reaction_set in enumerate(rxnComboList):
            new_model = deepcopy(self.base_model)

            for item in lists_of_rxns:
                new_model.listed_reactions = item
                new_model.optional_reactions = reaction_set
                self.models.append(deepcopy(new_model))

    def enumerate_initial_value_combinations(self):

        models = []
        for each in self.models:
            nodes = []
            value_lists = []
            for item in each.nodes:
                nodes.append(item)
                value_lists.append(each.nodes[item].initial)
            value_combinations = list(product(*value_lists))
            for i, item in enumerate(value_combinations):
                value_combinations[i] = list(item)
            for item in value_combinations:
                model = deepcopy(each)
                for i, every in enumerate(item):
                    model.nodes[nodes[i]].initial = [every]
                models.append(deepcopy(model))
        self.models = deepcopy(models)

    def build_models(self):
        model_index = 0
        if os.path.exists('output/' + self.models[0].name):
            shutil.rmtree('output/' + self.models[0].name)
        for n, model in enumerate(self.models):
            if len(model.optional_reactions) + len(model.required_reactions) \
                    + len(model.listed_reactions) > 0:
                ModelBuilder(model_index, model, self.obs, self.network_figs)
                model_index += 1


class ModelBuilder(Builder):
    """
    Build a PySB model.
    """
    def __init__(self, num, model, obs, network_figs):

        super(ModelBuilder, self).__init__()
        self.num = num
        self.current_model = model
        self.obs = obs
        self.network_figs = network_figs
        self.parsed_templates = defaultdict(lambda: defaultdict(list))
        self.parsed_obs_templates = defaultdict(lambda: defaultdict(list))
        self.parsed_exp_templates = defaultdict(lambda: defaultdict(list))
        self.parsed_reactions = []
        self.parsed_observables = []
        self.parsed_expressions = []
        self.reaction_tags = []
        self.reaction_rule_index = []
        self.reaction_types = []
        self.reaction_names = []
        self.fill_reactions = []
        self.reaction_parameter_values = []
        self.monomer_info = defaultdict(list)
        self.build()
        self.export()

    def text_rules(self, text):

        new_text = []
        new_monomers = []
        for line in text:
            if line[0:7] == 'Monomer':
                new_monomers.append(line.split('\'')[1])
            if line[0:4] != 'Rule':
                new_text.append(line)

            if line[0:4] == 'Rule':
                sp = []
                sp.append(line.split(',')[0])
                sp.append(','.join(line.split(',')[1:-1]))
                sp.append(line.split(',')[-1])
                monos = []
                for each in sp[1].split():
                    if '(' in each:
                        monos.append(each.split('(')[0])
                for each in monos:
                    if each not in new_monomers:
                        ismon = False
                        for item in self.model.monomers:
                            if item.name == each:
                                ismon = True

                        if not ismon:
                            self.monomer(each, [], {})

                parens = []
                for i, ch in enumerate(sp[1]):
                    if ch == '(':
                        parens.append([i])
                    if ch == ')':
                        parens[-1].append(i)

                for i, each in enumerate(monos):

                    sites = ''
                    record = False
                    for j, item in enumerate(sp[1]):
                        if j == parens[i][1]:
                            record = False
                        if record:
                            sites += item
                        if j == parens[i][0]:
                            record = True
                    ss = sites.split()

                    for j, item in enumerate(ss):
                        if item[-1] == ',':
                            ss[j] = ss[j][:-1]

                    sss = deepcopy(ss)
                    for j, item in enumerate(sss):
                        sss[j] = sss[j].split('=')[0]

                    ss_new = []
                    for item in self.model.monomers:
                        if item.name == each:
                            for j, every in enumerate(sss):
                                if every in item.sites:
                                    ss_new.append(ss[j])

                    ss_nj = ', '.join(ss_new)
                    new_sp1 = ''
                    copyover = True
                    for j, item in enumerate(sp[1]):
                        if j == parens[i][0]:
                            new_sp1 += item
                            copyover = False
                        if copyover:
                            new_sp1 += item

                        if j == parens[i][1]:
                            new_sp1 += ss_nj
                            new_sp1 += item
                            copyover = True
                    sp[1] = new_sp1

                sp = ','.join(sp)
                new_text.append(sp)

        return new_text

    def export(self):

        # write pre-text model
        if not os.path.exists('output/' + self.current_model.name):
            os.makedirs('output/' + self.current_model.name)

        f = open('output/' + self.current_model.name + '/model_' + str(self.num) + '.py', 'w+')
        f.write(PysbFlatExporter(self.model).export())
        f.close()

        # add top text
        f = open('output/' + self.current_model.name + '/model_' + str(self.num) + '.py', 'r')
        contents = f.readlines()
        f.close()

        self.current_model.text_top = self.text_rules(self.current_model.text_top)

        for i, each in enumerate(contents):
            if each.strip() == 'Model()':
                contents.insert(i, '\n')
                for j, line in enumerate(self.current_model.text_top):
                    contents.insert(i+j, line + '\n')
                break

        f = open('output/' + self.current_model.name + '/model_' + str(self.num) + '.py', 'w')
        for each in contents:
            f.write(each)
        f.close()

        # add bottom text
        self.current_model.text_bottom = self.text_rules(self.current_model.text_bottom)

        f = open('output/' + self.current_model.name + '/model_' + str(self.num) + '.py', 'a+')
        for line in self.current_model.text_bottom:
            f.write(line)
            f.write('\n')
        f.close()

        # add obs text
        f = open('output/' + self.current_model.name + '/model_' + str(self.num) + '.py', 'r')
        contents = f.readlines()
        f.close()

        obs_ind = 0
        for i, each in enumerate(contents):
            if "Observable" in each:
                obs_ind = i
        for i, each in enumerate(self.current_model.text_obs):
            contents.insert(i + obs_ind + 1, each + '\n')

        f = open('output/' + self.current_model.name + '/model_' + str(self.num) + '.py', 'w')
        for each in contents:
            f.write(each)
        f.close()

        # rule specific text
        params_to_remove = []
        f = open('output/' + self.current_model.name + '/model_' + str(self.num) + '.py', 'r')
        contents = f.readlines()
        f.close()

        expression_tags = []
        ex_tags_count = 0
        for each in self.reaction_tags:
            expression_tags.append([])
            for item in each:
                if item.split(':')[0] == 'expression':
                    expression_tags[-1].append(item)
                    ex_tags_count += 1

        while ex_tags_count > 0:
            rule_index = 0
            for i, each in enumerate(contents):
                if each[:4] == 'Rule':
                    expressions = []
                    rule_name = each.split("'")[1].strip()
                    rule_ind = 0
                    if expression_tags[rule_index]:
                        params = expression_tags[rule_index][0].split(':')[1].split('(')[1][:-1].split(';')
                        param_index = 0
                        param_names = []

                        # TODO: NEEDS PROPER PARSING
                        # TODO: NEEDS TO ALLOW FOR MULTIPLE EXPRESSIONS
                        for j, every in enumerate(self.current_model.text_library[expression_tags[rule_index][0].split(':')[1].split('(')[0].strip()]):
                            rule_ind = j
                            if every[:9] == 'Parameter':
                                param_names.append([every.split("'")[1], rule_name + '_' + every.split("'")[1].split('_')[1]])
                                every2 = 'Parameter(\'' + rule_name + '_' + every.split("'")[1].split('_')[1] + '\', ' + params[param_index] + ')\n'
                                param_index += 1
                                contents.insert(i+j, every2)
                            elif every[:10] == 'Expression':
                                for thing in param_names:
                                    if thing[0] in every:
                                        every = every.replace(thing[0], thing[1])
                                obs = []
                                for thing in params:
                                    if thing[-3:] == 'obs':
                                        obs.append(thing)
                                for k, thing in enumerate(obs):
                                    every = every.replace('obs_' + str(k), thing)
                                every = every.split("'")[0] + '\'' + rule_name + '_ex\'' + every.split("'")[2]
                                contents.insert(i+j, every)
                                expressions.append(every.split("'")[1])
                            else:
                                contents.insert(i+j, every)

                        # rename parameter for expression
                        if expressions:
                            rule_split = each.split(',')
                            for j, item in enumerate(expressions):
                                params_to_remove.append(
                                    rule_split[len(each.split(',')) - len(expressions) + j].split(')')[0].strip())
                                rule_split[len(each.split(',')) - len(expressions) + j] = ' ' + item
                            contents[i + rule_ind + 1] = ','.join(rule_split) + ')\n\n'

                        expression_tags[rule_index] = []
                        ex_tags_count -= 1
                        break
                    rule_index += 1

        # remove unneeded parameters
        new_contents = []
        for each in contents:
            retain = True
            for item in params_to_remove:
                if item in each:
                    retain = False
            if retain:
                new_contents.append(each)

        f.close()

        f = open('output/' + self.current_model.name + '/model_' + str(self.num) + '.py', 'w')
        for each in new_contents:
            f.write(each)
        f.close()

        # if self.network_figs:
        #
        #     filename = '/home/mak/PycharmProjects/HypBuilder3/output/' + self.current_model.name + '/model_' + str(self.num) + '.py'
        #     print(filename)
        #
        #     spec = importlib.util.spec_from_file_location('model_' + str(self.num) + '.py', 'output/' + self.current_model.name + '/model_' + str(self.num) + '.py')
        #     model = importlib.util.module_from_spec(spec)
        #     spec.loader.exec_module(model)
        #
        #     psv = PysbStaticViz(model.model)
        #     save_path = filename[:-3] + '.png'
        #     psv.networkx_draw(type_graph='observables', save_path=save_path, figsize=[15, 15], layout='spring_layout', **{'k': 1})
        #     # psv.networkx_draw(type_graph='species', save_path=save_path, layout='circular_layout', **{'seed': 1})


    def build(self):

        self.parse_templates()
        self.process_reactions()
        self.collect_monomer_info()
        self.add_monomers()
        self.fill_remaining_sites()
        self.add_observables()
        self.add_rules()
        self.add_initials()

    @staticmethod
    def is_float(string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    def parse_templates(self):

        # parse the reaction templates observables and expressions
        for molecule in self.current_model.library:
            for reaction in self.current_model.library[molecule]:
                self.parsed_templates[molecule][reaction] = []
                for template in self.current_model.library[molecule][reaction].templates:
                    molecules = re.split(r'\s*\|\s*|\s*>>\s*|\s*\+\s*|\s*<>\s*|\s*%\s*', template)
                    operations = re.findall(r'\s*\|\s*|\s*>>\s*|\s*\+\s*|\s*<>\s*|\s*%\s*', template)
                    parsed = []
                    for mols in molecules:

                        parsed.append([])
                        sites = []
                        states = []
                        if '(' in mols:
                            parsed[-1].append(mols[:mols.index('(')])
                            if '()' not in mols:
                                ms = re.split(r'\s*=\s*|\s*,\s*', mols[mols.index('(') + 1:-1])
                                sites.extend(ms[::2])
                                for s in ms[1::2]:
                                    states.append(s)
                        else:
                            parsed[-1].append(mols)
                        parsed[-1].append(sites)
                        parsed[-1].append(states)
                    parsed_rxn = [parsed.pop(0)]
                    for i, mols in enumerate(parsed):
                        parsed_rxn.append(operations[i].strip())
                        parsed_rxn.append(mols)
                    self.parsed_templates[molecule][reaction].append(parsed_rxn)

    def process_reactions(self):
        # collect required and optional reactions
        reactions_to_process = deepcopy(self.current_model.required_reactions)
        reactions_to_process.extend(deepcopy(self.current_model.optional_reactions))
        reactions_to_process.extend(deepcopy(self.current_model.listed_reactions))

        for each in reactions_to_process:

            # collect reaction, the molecules involved, and their molecule types from the model reactions.
            reaction = each[0]
            molecules = []
            site_labels = []
            site_values = []
            molecule_types = []
            tags = []
            types = []
            param_values = []

            for item in each[1:]:
                if ']' in item and '}' not in item:
                    molecules.append(item.split('[')[0].split('(')[0])
                    molecule_types.append(item.split('[')[1][:-1])
                    if item.split('(')[1].split(')')[0]:
                        labels = item.split('(')[1].split(')')[0].split(':')
                        no_eq_val = False
                        eq_val = False
                        for every in labels:
                            if '=' not in every:
                                no_eq_val = True
                                site_labels.append([every])
                            if '=' in every:
                                eq_val = True
                                site_values.append([every.split('=')])
                        if not no_eq_val:
                            site_labels.append([])
                        if not eq_val:
                            site_values.append([])
                    else:
                        site_labels.append([])
                        site_values.append([])
                elif '}' in item:
                    tgs = item.strip()[1:-1].split('|')
                    for every in tgs:
                        if every.split(':')[0] == 't':
                            types.append(every.split(':')[1])
                        else:
                            tags.append(every)
                else:
                    param_values.append(item.strip())

            # print
            # print molecules
            # print site_labels
            # print site_values
            # print molecule_types
            # print tags
            # print types
            # print param_values
            # print

            # from reaction template substitute the corresponding molecules
            for mt in molecule_types:
                if reaction in self.parsed_templates[mt] and self.parsed_templates[mt][reaction]:
                    for t, temp in enumerate(self.parsed_templates[mt][reaction]):
                        reaction_name = each[0] + '_' + str(t)
                        for elem in each[1:]:

                            if '[' in elem and '{' not in elem:
                                if '()' in elem:
                                    reaction_name += '_' + elem.split('[')[0].split('(')[0] + '_' + elem.split('[')[1][:-1]
                                else:
                                    site_str = elem.split('[')[0].split('(')[1].split(')')[0].split(':')
                                    for s, site in enumerate(site_str):
                                        if '=' in site:
                                            site_str[s] = '_'.join(site.split('='))
                                    site_str = '_'.join(site_str)
                                    reaction_name += '_' + elem.split('[')[0].split('(')[0] + '_' + elem.split('[')[1][:-1] + '_' + site_str

                        self.reaction_names.append(reaction_name)
                        rxn = deepcopy(temp)

                        for i, elem in enumerate(rxn):
                            if isinstance(elem, list) and elem[0] != 'None':
                                mol_ind = None

                                for j, mol_typ in enumerate(molecule_types):
                                    if elem[0] == mol_typ:
                                        mol_ind = deepcopy(j)
                                        rxn[i][0] = molecules[j]
                                for j, every in enumerate(elem[1]):
                                    if j <= len(site_labels[mol_ind])-1:
                                        rxn[i][1][j] = site_labels[mol_ind][j]
                                    else:
                                        for k, mol_typ in enumerate(molecule_types):
                                            if every == mol_typ:
                                                rxn[i][1][j] = molecules[k]
                                            if '_' in every and every.split('_')[0] == mol_typ \
                                                    and every.split('_')[1].isdigit():
                                                rxn[i][1][j] = molecules[k] + '_' + every.split('_')[1]
                                if site_values[mol_ind]:
                                    rxn[i][1].append(site_values[mol_ind][0][0])
                                    rxn[i][2].append(site_values[mol_ind][0][1])

                        self.reaction_tags.append(tags)
                        self.parsed_reactions.append(rxn)
                        self.reaction_types.append([])

                        if types:
                            typ = types.pop(0)
                            if '<>' in rxn or '|' in rxn:
                                self.reaction_types[-1].append(typ + 'f')
                                self.reaction_types[-1].append(typ + 'r')
                            else:
                                self.reaction_types[-1].append(typ + 'f')

                        # add reaction rates
                        self.reaction_parameter_values.append([])
                        if param_values:
                            if '<>' in rxn or '|' in rxn:
                                self.reaction_parameter_values[-1].append(param_values.pop(0))
                                self.reaction_parameter_values[-1].append(param_values.pop(0))
                            else:
                                self.reaction_parameter_values[-1].append(param_values.pop(0))
                        else:
                            if '<>' in rxn or '|' in rxn:
                                self.reaction_parameter_values[-1].extend(['vary', 'vary'])
                            else:
                                self.reaction_parameter_values[-1].extend(['vary'])

            self.reaction_rule_index.append(len(self.parsed_reactions))

    def collect_monomer_info(self):

        # fill monomer info
        for each in self.parsed_reactions:
            for item in each:
                if isinstance(item, list):
                    if item[0] != 'None':
                        if item[0] not in self.monomer_info:
                            self.monomer_info[item[0]] = []
                        for every in item[1]:
                            if every not in self.monomer_info[item[0]]:
                                self.monomer_info[item[0]].append(every)

    def add_monomers(self):

        # create monomers
        for each in self.monomer_info:
            self.monomer(each, self.monomer_info[each], {})


    def fill_remaining_sites(self):

        # fill out monomer binding sites
        for i, rxn in enumerate(self.parsed_reactions):
            dwdc = []
            for j, tag in enumerate(self.reaction_tags[i]):
                if tag:
                    tag_split = tag.split(':')
                    if tag_split[0] == 'dwdc':
                        dwdc.extend(tag_split[1:])
            for j, elem in enumerate(dwdc):
                if '(' in elem:
                    dwdc[j] = dwdc[j].split('(')
                    dwdc[j][1] = dwdc[j][1][:-1].split(',')

            for j, elem in enumerate(rxn):
                if isinstance(elem, list):
                    if elem[0] != 'None':
                        for site in self.monomer_info[elem[0]]:
                            add_site = True
                            for every in dwdc:
                                if elem[0] == every[0] and site in every[1]:
                                    add_site = False
                            if add_site and site not in self.parsed_reactions[i][j][1]:
                                self.parsed_reactions[i][j][1].append(site)
                                self.parsed_reactions[i][j][2].append('None')

    def add_rules(self):
        for i, rxn in enumerate(self.parsed_reactions):

            # substitute in integers, None, ANY, and WILD
            for k, item in enumerate(rxn):
                if item != '+' and item != '%' and item != '>>' and item != '<>' and item != '|':

                    for j, every in enumerate(item[2]):
                        if every == 'None':
                            rxn[k][2][j] = None
                        if every == 'ANY':
                            rxn[k][2][j] = ANY
                        if every == 'WILD':
                            rxn[k][2][j] = WILD
                        if every.isdigit():
                            rxn[k][2][j] = int(every)

            # define monomer patterns
            mon_pats = []
            for elem in rxn:
                if elem == '+' or elem == '%' or elem == '>>' or elem == '<>' or elem == '|':
                    mon_pats.append(elem)
                else:
                    if elem[0] == 'None':
                        mon_pats.append('None')
                    else:
                        mon_states = {}
                        for j, every in enumerate(elem[1]):
                            mon_states[every] = elem[2][j]
                        mon_obj = self.model.monomers[elem[0]]
                        mon_pats.append(MonomerPattern(mon_obj, mon_states, None))

            # define complex patterns
            com_pats_temp = [[]]
            for item in mon_pats:
                if item == '>>' or item == '<>' or item == '|':
                    com_pats_temp.extend([item, []])
                elif item == '+':
                    com_pats_temp.append([])
                elif item == '%':
                    pass
                else:
                    com_pats_temp[-1].append(item)

            com_pats = []
            for item in com_pats_temp:
                if item == '>>' or item == '<>' or item == '|':
                    com_pats.append(item)
                elif item == ['None']:
                    pass
                else:
                    com_pats.append(ComplexPattern(item, None))

            # define reversibility and split patterns into reactants and products
            react_com_pats = []
            prod_com_pats = []
            mark = 0
            reversible = None
            for item in com_pats:
                if item == '<>' or item == '|':
                    mark = 1
                    reversible = True
                elif item == '>>':
                    mark = 1
                    reversible = False
                else:
                    if mark == 0:
                        react_com_pats.append(item)
                    if mark == 1:
                        prod_com_pats.append(item)
            order = [len(react_com_pats), len(prod_com_pats)]

            # define rule expression
            rule_exp = RuleExpression(ReactionPattern(react_com_pats), ReactionPattern(prod_com_pats), reversible)

            suffix0 = '_0'
            suffix1 = '_0'
            if self.reaction_types[i]:
                if reversible:
                    suffix0 = self.reaction_types[i][0]
                    suffix1 = self.reaction_types[i][1]
                else:
                    suffix0 = self.reaction_types[i][0]

            # add rules to the model
            if self.reaction_types[i]:
                if reversible:

                    if self.is_float(self.reaction_parameter_values[i][0]):
                        forward = self.reaction_names[i] + '_' + str(order[0]) + suffix0 + '_0'
                        self.parameter(forward, self.reaction_parameter_values[i][0])
                    else:
                        forward = self.reaction_names[i] + '_' + str(order[0]) + suffix0
                        self.parameter(forward, 1)

                    if self.is_float(self.reaction_parameter_values[i][1]):
                        reverse = self.reaction_names[i] + '_' + str(order[1]) + suffix1 + '_0'
                        self.parameter(reverse, self.reaction_parameter_values[i][1])
                    else:
                        reverse = self.reaction_names[i] + '_' + str(order[1]) + suffix1
                        self.parameter(reverse, 1)

                    self.rule(self.reaction_names[i], rule_exp, self.model.parameters[forward],
                              self.model.parameters[reverse])
                else:
                    if self.is_float(self.reaction_parameter_values[i][0]):
                        forward = self.reaction_names[i] + '_' + str(order[0]) + suffix0 + '_0'
                        self.parameter(forward, self.reaction_parameter_values[i][0])
                    else:
                        forward = self.reaction_names[i] + '_' + str(order[0]) + suffix0
                        self.parameter(forward, 1)

                    self.rule(self.reaction_names[i], rule_exp, self.model.parameters[forward])

            else:
                if reversible:

                    if self.is_float(self.reaction_parameter_values[i][0]):
                        forward = self.reaction_names[i] + '_' + str(order[0]) + 'kf' + '_0'
                        self.parameter(forward, self.reaction_parameter_values[i][0])
                    else:
                        forward = self.reaction_names[i] + '_' + str(order[0]) + 'kf'
                        self.parameter(forward, 1)

                    if self.is_float(self.reaction_parameter_values[i][1]):
                        reverse = self.reaction_names[i] + '_' + str(order[1]) + 'kr' + '_0'
                        self.parameter(reverse, self.reaction_parameter_values[i][1])
                    else:
                        reverse = self.reaction_names[i] + '_' + str(order[1]) + 'kr'
                        self.parameter(reverse, 1)

                    self.rule(self.reaction_names[i], rule_exp, self.model.parameters[forward],
                              self.model.parameters[reverse])
                else:
                    if order[1] == 1:
                        if self.is_float(self.reaction_parameter_values[i][0]):
                            forward = self.reaction_names[i] + '_' + str(order[0]) + 'kf' + '_0'
                            self.parameter(forward, self.reaction_parameter_values[i][0])
                        else:
                            forward = self.reaction_names[i] + '_' + str(order[0]) + 'kf'
                            self.parameter(forward, 1)

                        self.rule(self.reaction_names[i], rule_exp, self.model.parameters[forward])
                    else:
                        if self.is_float(self.reaction_parameter_values[i][0]):
                            forward = self.reaction_names[i] + '_' + str(order[0]) + 'kc' + '_0'
                            self.parameter(forward, self.reaction_parameter_values[i][0])
                        else:
                            forward = self.reaction_names[i] + '_' + str(order[0]) + 'kc'
                            self.parameter(forward, 1)

                        self.rule(self.reaction_names[i], rule_exp, self.model.parameters[forward])

    @staticmethod
    def random_binding(mols, pairs, binds):

        # This function randomly selects binding pairs until no more binding partners are available
        pair_num = [i for i in range(len(pairs))]
        while True:
            pairs_p = []
            for each in pairs:
                pairs_p.append(mols[each[0]] * mols[each[1]])
            s = sum(pairs_p)
            if not s:
                break
            pairs_p[:] = [float(x) / s for x in pairs_p]
            pair = choice(pair_num, 1, p=pairs_p)[0]
            mols[pairs[pair][0]] -= 1
            mols[pairs[pair][1]] -= 1
            binds[pair] += 1

    def add_initials(self):

        # adjust prioritized IVs

        priorities = defaultdict(list)

        for each in self.monomer_info:
            if self.current_model.iv_priorities[each]:
                for item in self.current_model.iv_priorities[each]:
                    priorities[item[0]].append([item[1], each])

        for each in priorities:
            priorities[each] = sorted(priorities[each])
            value_used = False
            for item in priorities:
                for every in priorities[item]:
                    if every[1] in self.monomer_info and not value_used:
                        self.current_model.nodes[every[1]].initial[0] = self.current_model.nodes[every[1]].initial[0]
                        value_used = True
                    else:
                        self.current_model.nodes[every[1]].initial[0] = 0

        for each in self.current_model.nodes:
            self.current_model.nodes[each].initial[0] = float(self.current_model.nodes[each].initial[0])

        # finds binding reactions that should be initialized as bound (maxed)
        binding_rxn_list = []
        for i, each in enumerate(self.reaction_tags):
            for item in each:
                if 'f' in item:
                    if '%' in self.parsed_reactions[i]:
                        binding_rxn_list.append([self.parsed_reactions[i], item.split(':')[1]])

        # adjusts iv's for bound monomers and initialize bound species
        max_molecules = []
        max_binding_pairs = []
        
        specific_molecules = []
        specific_binding_pairs = []
        specific_binding_quant = []

        for each in binding_rxn_list:
            if each[1] == 'all':
                if each[0][0][0] not in max_molecules:
                    max_molecules.append(each[0][0][0])
                if each[0][2][0] not in max_molecules:
                    max_molecules.append(each[0][2][0])
            if each[1].isdigit():
                if each[0][0][0] not in specific_molecules:
                    specific_molecules.append(each[0][0][0])
                if each[0][2][0] not in specific_molecules:
                    specific_molecules.append(each[0][2][0])

        for each in binding_rxn_list:
            if each[1] == 'all':
                ind_1 = max_molecules.index(each[0][0][0])
                ind_2 = max_molecules.index(each[0][2][0])
                max_binding_pairs.append([ind_1, ind_2])
            if each[1].isdigit():
                ind_1 = specific_molecules.index(each[0][0][0])
                ind_2 = specific_molecules.index(each[0][2][0])
                specific_binding_pairs.append([ind_1, ind_2])
                specific_binding_quant.append(float(each[1]))

        # rearrange quantities for max binding
        max_molecule_quant = []
        max_binding_quant = [0 for _ in max_binding_pairs]
        for each in max_molecules:
            max_molecule_quant.append(self.current_model.nodes[each].initial[0])
        self.random_binding(max_molecule_quant, max_binding_pairs, max_binding_quant)
        for i, each in enumerate(max_molecules):
            self.current_model.nodes[each].initial[0] = max_molecule_quant[i]

        # rearrange quantities for specific binding
        specific_molecule_quant = []
        for each in specific_molecules:
            specific_molecule_quant.append(self.current_model.nodes[each].initial[0])

        for i, each in enumerate(specific_binding_quant):
            if each > specific_molecule_quant[specific_binding_pairs[i][0]] \
                    or each > specific_molecule_quant[specific_binding_pairs[i][1]]:

                print('The specified number for the bound species %s %% %s is %s.\n The number of molecules for %s and'
                      ' %s are %s and %s repectively. \nThe number of molecules for both monomers must be at least as '
                      'great as the specified munber of the bound species.',
                      specific_molecules[specific_binding_pairs[i][0]],
                      specific_molecules[specific_binding_pairs[i][1]],
                      str(each), specific_molecules[specific_binding_pairs[i][0]],
                      specific_molecules[specific_binding_pairs[i][1]],
                      specific_molecule_quant[specific_binding_pairs[i][0]],
                      specific_molecule_quant[specific_binding_pairs[i][1]])
                quit()

            specific_molecule_quant[specific_binding_pairs[i][0]] -= each
            specific_molecule_quant[specific_binding_pairs[i][1]] -= each
        for i, each in enumerate(specific_molecules):
            self.current_model.nodes[each].initial[0] = specific_molecule_quant[i]

        bond_num = 1

        for i, each in enumerate(max_binding_pairs):
            init_name = max_molecules[each[0]] + '_' + max_molecules[each[1]] + '_0'
            mon_obj_1 = self.model.monomers[max_molecules[each[0]]]
            mon_obj_2 = self.model.monomers[max_molecules[each[1]]]
            states_1 = {}
            states_2 = {}
            self.parameter(init_name, max_binding_quant[i])

            for item in mon_obj_1.sites:
                if item == max_molecules[each[1]]:
                    states_1[item] = bond_num
                elif '_' in item and item.split('_')[0] == max_molecules[each[1]]:
                    states_1[item] = bond_num
                else:
                    states_1[item] = None

            for item in mon_obj_2.sites:
                if item == max_molecules[each[0]]:
                    states_2[item] = bond_num
                elif '_' in item and item.split('_')[0] == max_molecules[each[0]]:
                    states_1[item] = bond_num
                    bond_num += 1
                else:
                    states_2[item] = None

            self.initial(ComplexPattern([MonomerPattern(mon_obj_1, states_1, None),
                                         MonomerPattern(mon_obj_2, states_2, None)], None),
                         self.model.parameters[init_name])

        for i, each in enumerate(specific_binding_pairs):
            init_name = specific_molecules[each[0]] + '_' + specific_molecules[each[1]] + '_0'
            mon_obj_1 = self.model.monomers[specific_molecules[each[0]]]
            mon_obj_2 = self.model.monomers[specific_molecules[each[1]]]
            states_1 = {}
            states_2 = {}
            self.parameter(init_name, specific_binding_quant[i])

            for item in mon_obj_1.sites:
                if item == specific_molecules[each[1]]:
                    states_1[item] = bond_num
                elif '_' in item and item.split('_')[0] == specific_molecules[each[1]]:
                    states_1[item] = bond_num
                else:
                    states_1[item] = None

            for item in mon_obj_2.sites:
                if item == specific_molecules[each[0]]:
                    states_2[item] = bond_num
                elif '_' in item and item.split('_')[0] == specific_molecules[each[0]]:
                    states_1[item] = bond_num
                    bond_num += 1
                else:
                    states_2[item] = None

            self.initial(ComplexPattern([MonomerPattern(mon_obj_1, states_1, None),
                                         MonomerPattern(mon_obj_2, states_2, None)], None),
                         self.model.parameters[init_name])

        # initialize monomers
        for each in self.monomer_info:
            init_name = each + '_0'
            mon_obj = self.model.monomers[each]
            states = {}

            if self.current_model.nodes[each].initial:
                self.parameter(init_name, self.current_model.nodes[each].initial[0])
            else:
                self.parameter(init_name, 0)

            for item in mon_obj.sites:
                states[item] = None

            self.initial(MonomerPattern(mon_obj, states, None), self.model.parameters[init_name])

    def add_observables(self):

        # add observable for each monomer in model
        if self.obs == 'monomers':
            for each in self.monomer_info:
                obs_name = each + '_obs'
                self.observable(obs_name, self.model.monomers[each])

        # add all species as observables
        if self.obs == 'species':
            generate_equations(self.model)
            for each in self.model.species:

                species = str(each)
                obs_name = ''
                app = True
                for char in species:
                    if char == '(':
                        obs_name += '_'
                    if app and char != '(' and char != ')' and char != '=' and char != ',' and char != ' ' and char != '%':
                        obs_name += char
                    if char == '=':
                        obs_name += '_'
                    if char == ',':
                        obs_name += '_'
                    if char == '%':
                        obs_name += '__'
                obs_name += '_obs'

                self.observable(obs_name, each)
