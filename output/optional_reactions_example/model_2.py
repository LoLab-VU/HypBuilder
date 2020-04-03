# exported from PySB model 'model'

from pysb import Model, Monomer, Parameter, Expression, Compartment, Rule, Observable, Initial, MatchOnce, Annotation, MultiState, Tag, ANY, WILD


Model()

Monomer('D', ['E'])
Monomer('E', ['D'])
Monomer('A', ['C'])
Monomer('C', ['A'])

Parameter('inhibition_0_D_inhibitor_E_inh_target_2kf', 1.0)
Parameter('inhibition_0_D_inhibitor_E_inh_target_1kr', 1.0)
Parameter('inhibition_0_A_inhibitor_C_inh_target_2kf', 1.0)
Parameter('inhibition_0_A_inhibitor_C_inh_target_1kr', 1.0)
Parameter('D_0', 1.0)
Parameter('E_0', 1.0)
Parameter('A_0', 1.0)
Parameter('C_0', 1.0)

Observable('D_obs', D())
Observable('E_obs', E())
Observable('A_obs', A())
Observable('C_obs', C())

Rule('inhibition_0_D_inhibitor_E_inh_target', D(E=None) + E(D=None) | D(E=1) % E(D=1), inhibition_0_D_inhibitor_E_inh_target_2kf, inhibition_0_D_inhibitor_E_inh_target_1kr)
Rule('inhibition_0_A_inhibitor_C_inh_target', A(C=None) + C(A=None) | A(C=1) % C(A=1), inhibition_0_A_inhibitor_C_inh_target_2kf, inhibition_0_A_inhibitor_C_inh_target_1kr)

Initial(D(E=None), D_0)
Initial(E(D=None), E_0)
Initial(A(C=None), A_0)
Initial(C(A=None), C_0)

