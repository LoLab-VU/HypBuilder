# exported from PySB model 'model'

from pysb import Model, Monomer, Parameter, Expression, Compartment, Rule, Observable, Initial, MatchOnce, Annotation, ANY, WILD

Model()

Monomer('Noxa', ['Mcl1'])
Monomer('BAR', ['C8A'])
Monomer('BclxLM', ['BidM', 'BaxA', 'BakA', 'Bad'])
Monomer('BaxM', ['BidM', 'BaxA'])
Monomer('C8A', ['BidU', 'BAR', 'C3pro'])
Monomer('XIAP', ['Apop', 'SmacA', 'C3A'])
Monomer('DISC', ['C8pro', 'flip'])
Monomer('SmacM', ['BaxA', 'BakA'])
Monomer('C6pro', ['C3A'])
Monomer('Apop', ['C3pro', 'XIAP'])
Monomer('SmacA', ['XIAP'])
Monomer('SmacC')
Monomer('PARPU', ['C3A'])
Monomer('C9')
Monomer('Bad', ['Bcl2', 'BclxLM'])
Monomer('C3ub')
Monomer('C8pro', ['DISC', 'C6A'])
Monomer('PARPC')
Monomer('L', ['R'])
Monomer('C3pro', ['Apop', 'C8A'])
Monomer('R', ['L'])
Monomer('Mcl1', ['BidM', 'BakA', 'Noxa'])
Monomer('CytoCA', ['ApafI'])
Monomer('CytoCC')
Monomer('BakA', ['BakM', 'BclxLM', 'Mcl1', 'BakA_1', 'BakA_2', 'CytoCM', 'SmacM'])
Monomer('BaxC')
Monomer('BaxA', ['BaxM', 'Bcl2', 'BclxLM', 'BaxA_1', 'BaxA_2', 'CytoCM', 'SmacM'])
Monomer('ApafI', ['CytoCA'])
Monomer('Bcl2', ['BidM', 'BaxA', 'Bad'])
Monomer('BidU', ['C8A'])
Monomer('BidT')
Monomer('C3A', ['XIAP', 'PARPU', 'C6pro'])
Monomer('flip', ['DISC'])
Monomer('ApafA')
Monomer('BidM', ['BaxM', 'BakM', 'Bcl2', 'BclxLM', 'Mcl1'])
Monomer('BakM', ['BidM', 'BakA'])
Monomer('C6A', ['C8pro'])
Monomer('BclxLC')
Monomer('CytoCM', ['BaxA', 'BakA'])

Parameter('dimerization_0_L_subunit_a_R_subunit_b_DISC_dimer_2kf_0', 4.861071716904088e-09)
Parameter('dimerization_0_L_subunit_a_R_subunit_b_DISC_dimer_1kr_0', 6.998465115734616e-05)
Parameter('dimerization_1_L_subunit_a_R_subunit_b_DISC_dimer_1kf_0', 0.0001004038401598357)
Parameter('catalysis_0_DISC_catalyzer_C8pro_substrate_C8A_product_2kf_0', 1.652610985853028e-06)
Parameter('catalysis_0_DISC_catalyzer_C8pro_substrate_C8A_product_1kr_0', 0.00025515949741149136)
Parameter('catalysis_1_DISC_catalyzer_C8pro_substrate_C8A_product_1kc_0', 8.103548380745098)
Parameter('catalysis_0_C8A_catalyzer_BidU_substrate_BidT_product_2kf_0', 7.86934184773797e-06)
Parameter('catalysis_0_C8A_catalyzer_BidU_substrate_BidT_product_1kr_0', 1.3478527255190856e-05)
Parameter('catalysis_1_C8A_catalyzer_BidU_substrate_BidT_product_1kc_0', 0.20070834648071373)
Parameter('inhibition_0_flip_inhibitor_DISC_inh_target_2kf_0', 2.085720709467102e-06)
Parameter('inhibition_0_flip_inhibitor_DISC_inh_target_1kr_0', 0.07299308187409242)
Parameter('inhibition_0_BAR_inhibitor_C8A_inh_target_2kf_0', 2.450754439292685e-05)
Parameter('inhibition_0_BAR_inhibitor_C8A_inh_target_1kr_0', 3.176107099863868e-05)
Parameter('equilibration_0_SmacC_equil_a_SmacA_equil_b_1kf_0', 0.6866765861741175)
Parameter('equilibration_0_SmacC_equil_a_SmacA_equil_b_1kr_0', 0.0007785344594901969)
Parameter('equilibration_0_CytoCC_equil_a_CytoCA_equil_b_1kf_0', 0.020412343795425145)
Parameter('equilibration_0_CytoCC_equil_a_CytoCA_equil_b_1kr_0', 0.002507160753472891)
Parameter('catalysis_0_CytoCA_catalyzer_ApafI_substrate_ApafA_product_2kf_0', 4.592758585213764e-07)
Parameter('catalysis_0_CytoCA_catalyzer_ApafI_substrate_ApafA_product_1kr_0', 2.8999962220310582e-05)
Parameter('catalysis_1_CytoCA_catalyzer_ApafI_substrate_ApafA_product_1kc_0', 0.04059971791806174)
Parameter('conversion_0_C9_subunit_d_ApafA_subunit_c_Apop_complex_2kf_0', 3.213196857547145e-07)
Parameter('conversion_0_C9_subunit_d_ApafA_subunit_c_Apop_complex_1kr_0', 0.011684477645560146)
Parameter('catalysis_0_Apop_catalyzer_C3pro_substrate_C3A_product_2kf_0', 7.803769100546674e-10)
Parameter('catalysis_0_Apop_catalyzer_C3pro_substrate_C3A_product_1kr_0', 0.0003280248182331038)
Parameter('catalysis_1_Apop_catalyzer_C3pro_substrate_C3A_product_1kc_0', 1.1684643810480766)
Parameter('inhibition_0_XIAP_inhibitor_Apop_inh_target_2kf_0', 2.070453553168279e-08)
Parameter('inhibition_0_XIAP_inhibitor_Apop_inh_target_1kr_0', 0.0013859740873431536)
Parameter('inhibition_0_SmacA_inhibitor_XIAP_inh_target_2kf_0', 0.0004094401791751448)
Parameter('inhibition_0_SmacA_inhibitor_XIAP_inh_target_1kr_0', 0.008005113495400151)
Parameter('catalysis_0_C8A_catalyzer_C3pro_substrate_C3A_product_2kf_0', 1.916761911426892e-06)
Parameter('catalysis_0_C8A_catalyzer_C3pro_substrate_C3A_product_1kr_0', 0.00010186532359752733)
Parameter('catalysis_1_C8A_catalyzer_C3pro_substrate_C3A_product_1kc_0', 2.7002149431488567)
Parameter('catalysis_0_XIAP_catalyzer_C3A_substrate_C3ub_product_2kf_0', 1.8247861512403385e-07)
Parameter('catalysis_0_XIAP_catalyzer_C3A_substrate_C3ub_product_1kr_0', 1.2921875123372521e-05)
Parameter('catalysis_1_XIAP_catalyzer_C3A_substrate_C3ub_product_1kc_0', 0.09950498063157984)
Parameter('catalysis_0_C3A_catalyzer_PARPU_substrate_PARPC_product_2kf_0', 1.889526802914492e-06)
Parameter('catalysis_0_C3A_catalyzer_PARPU_substrate_PARPC_product_1kr_0', 0.00011387916767652634)
Parameter('catalysis_1_C3A_catalyzer_PARPU_substrate_PARPC_product_1kc_0', 13.768204206283402)
Parameter('catalysis_0_C3A_catalyzer_C6pro_substrate_C6A_product_2kf_0', 2.1334646851306905e-08)
Parameter('catalysis_0_C3A_catalyzer_C6pro_substrate_C6A_product_1kr_0', 0.0015363069332776634)
Parameter('catalysis_1_C3A_catalyzer_C6pro_substrate_C6A_product_1kc_0', 13.054054125378238)
Parameter('catalysis_0_C6A_catalyzer_C8pro_substrate_C8A_product_2kf_0', 5.0560841288642224e-08)
Parameter('catalysis_0_C6A_catalyzer_C8pro_substrate_C8A_product_1kr_0', 9.197739657508746e-05)
Parameter('catalysis_1_C6A_catalyzer_C8pro_substrate_C8A_product_1kc_0', 0.1848860702109268)
Parameter('equilibration_0_BidT_equil_a_BidM_equil_b_1kf_0', 0.026956531627050594)
Parameter('equilibration_0_BidT_equil_a_BidM_equil_b_1kr_0', 1.1783387334989619e-05)
Parameter('equilibration_0_BaxC_equil_a_BaxM_equil_b_1kf_0', 0.0003405873853519951)
Parameter('equilibration_0_BaxC_equil_a_BaxM_equil_b_1kr_0', 0.04975033218452526)
Parameter('equilibration_0_BclxLC_equil_a_BclxLM_equil_b_1kf_0', 0.0684005644509762)
Parameter('equilibration_0_BclxLC_equil_a_BclxLM_equil_b_1kr_0', 0.14118753123479355)
Parameter('catalysis_0_BidM_catalyzer_BaxM_substrate_BaxA_product_2kf_0', 3.973677594697006e-09)
Parameter('catalysis_0_BidM_catalyzer_BaxM_substrate_BaxA_product_1kr_0', 0.021482642730885865)
Parameter('catalysis_1_BidM_catalyzer_BaxM_substrate_BaxA_product_1kc_0', 1.8203763301683924)
Parameter('catalysis_0_BidM_catalyzer_BakM_substrate_BakA_product_2kf_0', 1.9408461301064605e-09)
Parameter('catalysis_0_BidM_catalyzer_BakM_substrate_BakA_product_1kr_0', 0.00018094808868168103)
Parameter('catalysis_1_BidM_catalyzer_BakM_substrate_BakA_product_1kc_0', 0.011177441271776072)
Parameter('self_catalyze_0_BaxA_self_catalyzer_BaxM_self_substrate_2kf_0', 2.0149060250585873e-06)
Parameter('self_catalyze_0_BaxA_self_catalyzer_BaxM_self_substrate_1kr_0', 0.040311275999739105)
Parameter('self_catalyze_1_BaxA_self_catalyzer_BaxM_self_substrate_1kc_0', 0.012192887363178946)
Parameter('self_catalyze_0_BakA_self_catalyzer_BakM_self_substrate_2kf_0', 5.393982462632218e-06)
Parameter('self_catalyze_0_BakA_self_catalyzer_BakM_self_substrate_1kr_0', 0.002166628073982069)
Parameter('self_catalyze_1_BakA_self_catalyzer_BakM_self_substrate_1kc_0', 0.2647547364387896)
Parameter('inhibition_0_Bcl2_inhibitor_BidM_inh_target_2kf_0', 1.0277423337470143e-06)
Parameter('inhibition_0_Bcl2_inhibitor_BidM_inh_target_1kr_0', 2.7905757973936867)
Parameter('inhibition_0_BclxLM_inhibitor_BidM_inh_target_2kf_0', 1.6367225985110056e-07)
Parameter('inhibition_0_BclxLM_inhibitor_BidM_inh_target_1kr_0', 0.026264964906836046)
Parameter('inhibition_0_Mcl1_inhibitor_BidM_inh_target_2kf_0', 1.9428423606297654e-06)
Parameter('inhibition_0_Mcl1_inhibitor_BidM_inh_target_1kr_0', 0.0021648330129469106)
Parameter('inhibition_0_Bcl2_inhibitor_BaxA_inh_target_2kf_0', 1.4531081303335626e-08)
Parameter('inhibition_0_Bcl2_inhibitor_BaxA_inh_target_1kr_0', 0.07191752928301738)
Parameter('inhibition_0_BclxLM_inhibitor_BaxA_inh_target_2kf_0', 1.2086000195405126e-06)
Parameter('inhibition_0_BclxLM_inhibitor_BaxA_inh_target_1kr_0', 0.019684909992630065)
Parameter('inhibition_0_BclxLM_inhibitor_BakA_inh_target_2kf_0', 6.267454571958542e-06)
Parameter('inhibition_0_BclxLM_inhibitor_BakA_inh_target_1kr_0', 0.06729858838914062)
Parameter('inhibition_0_Mcl1_inhibitor_BakA_inh_target_2kf_0', 1.2661363465041514e-05)
Parameter('inhibition_0_Mcl1_inhibitor_BakA_inh_target_1kr_0', 0.0002157216265888175)
Parameter('inhibition_0_Bad_inhibitor_Bcl2_inh_target_2kf_0', 5.393106718143353e-05)
Parameter('inhibition_0_Bad_inhibitor_Bcl2_inh_target_1kr_0', 0.4401337807073528)
Parameter('inhibition_0_Bad_inhibitor_BclxLM_inh_target_2kf_0', 4.187752996931018e-05)
Parameter('inhibition_0_Bad_inhibitor_BclxLM_inh_target_1kr_0', 0.16263349657520218)
Parameter('inhibition_0_Noxa_inhibitor_Mcl1_inh_target_2kf_0', 6.119738462753812e-07)
Parameter('inhibition_0_Noxa_inhibitor_Mcl1_inh_target_1kr_0', 0.01966269798058537)
Parameter('pore_formation_0_BaxA_pore_2kf_0', 0.006742928757400231)
Parameter('pore_formation_0_BaxA_pore_1kr_0', 1.6822795105298417e-05)
Parameter('pore_formation_1_BaxA_pore_2kf_0', 0.00029378841202344446)
Parameter('pore_formation_1_BaxA_pore_1kr_0', 0.000144616)
Parameter('pore_formation_2_BaxA_pore_2kf_0', 8.5651e-05)
Parameter('pore_formation_2_BaxA_pore_1kr_0', 0.002585238)
Parameter('pore_formation_0_BakA_pore_2kf_0', 1.605416408848411e-05)
Parameter('pore_formation_0_BakA_pore_1kr_0', 0.00023979936345611174)
Parameter('pore_formation_1_BakA_pore_2kf_0', 5.741580455655337e-06)
Parameter('pore_formation_1_BakA_pore_1kr_0', 0.021389853)
Parameter('pore_formation_2_BakA_pore_2kf_0', 1.509873703e-05)
Parameter('pore_formation_2_BakA_pore_1kr_0', 1.538796535e-05)
Parameter('transport_0_BaxA_pore_CytoCM_cargo_M_CytoCC_cargo_C_2kf_0', 0.000106028)
Parameter('transport_0_BaxA_pore_CytoCM_cargo_M_CytoCC_cargo_C_1kr_0', 0.0013725161741816323)
Parameter('transport_1_BaxA_pore_CytoCM_cargo_M_CytoCC_cargo_C_1kc_0', 727.3165367902302)
Parameter('transport_0_BaxA_pore_SmacM_cargo_M_SmacC_cargo_C_2kf_0', 2.375382573e-06)
Parameter('transport_0_BaxA_pore_SmacM_cargo_M_SmacC_cargo_C_1kr_0', 0.0003693677240187805)
Parameter('transport_1_BaxA_pore_SmacM_cargo_M_SmacC_cargo_C_1kc_0', 83.18212226517896)
Parameter('transport_0_BakA_pore_CytoCM_cargo_M_CytoCC_cargo_C_2kf_0', 3.54927953e-07)
Parameter('transport_0_BakA_pore_CytoCM_cargo_M_CytoCC_cargo_C_1kr_0', 0.051294040280582424)
Parameter('transport_1_BakA_pore_CytoCM_cargo_M_CytoCC_cargo_C_1kc_0', 1.0588991714689346)
Parameter('transport_0_BakA_pore_SmacM_cargo_M_SmacC_cargo_C_2kf_0', 2.40631696e-05)
Parameter('transport_0_BakA_pore_SmacM_cargo_M_SmacC_cargo_C_1kr_0', 0.0006188430885970239)
Parameter('transport_1_BakA_pore_SmacM_cargo_M_SmacC_cargo_C_1kc_0', 16.739408086871173)
Parameter('Noxa_0', 0.0)
Parameter('BAR_0', 1000.0)
Parameter('BclxLM_0', 0.0)
Parameter('BaxM_0', 0.0)
Parameter('C8A_0', 0.0)
Parameter('XIAP_0', 100000.0)
Parameter('DISC_0', 0.0)
Parameter('SmacM_0', 100000.0)
Parameter('C6pro_0', 10000.0)
Parameter('Apop_0', 0.0)
Parameter('SmacA_0', 0.0)
Parameter('SmacC_0', 0.0)
Parameter('PARPU_0', 1000000.0)
Parameter('C9_0', 100000.0)
Parameter('Bad_0', 1000.0)
Parameter('C3ub_0', 0.0)
Parameter('C8pro_0', 20000.0)
Parameter('PARPC_0', 0.0)
Parameter('L_0', 3000.0)
Parameter('C3pro_0', 10000.0)
Parameter('R_0', 200.0)
Parameter('Mcl1_0', 20000.0)
Parameter('CytoCA_0', 0.0)
Parameter('CytoCC_0', 0.0)
Parameter('BakA_0', 0.0)
Parameter('BaxC_0', 80000.0)
Parameter('BaxA_0', 0.0)
Parameter('ApafI_0', 100000.0)
Parameter('Bcl2_0', 20000.0)
Parameter('BidU_0', 40000.0)
Parameter('BidT_0', 0.0)
Parameter('C3A_0', 0.0)
Parameter('flip_0', 100.0)
Parameter('ApafA_0', 0.0)
Parameter('BidM_0', 0.0)
Parameter('BakM_0', 20000.0)
Parameter('C6A_0', 0.0)
Parameter('BclxLC_0', 20000.0)
Parameter('CytoCM_0', 500000.0)

Observable('Noxa_obs', Noxa())
Observable('BAR_obs', BAR())
Observable('BclxLM_obs', BclxLM())
Observable('BaxM_obs', BaxM())
Observable('C8A_obs', C8A())
Observable('XIAP_obs', XIAP())
Observable('DISC_obs', DISC())
Observable('SmacM_obs', SmacM())
Observable('C6pro_obs', C6pro())
Observable('Apop_obs', Apop())
Observable('SmacA_obs', SmacA())
Observable('SmacC_obs', SmacC())
Observable('PARPU_obs', PARPU())
Observable('C9_obs', C9())
Observable('Bad_obs', Bad())
Observable('C3ub_obs', C3ub())
Observable('C8pro_obs', C8pro())
Observable('PARPC_obs', PARPC())
Observable('L_obs', L())
Observable('C3pro_obs', C3pro())
Observable('R_obs', R())
Observable('Mcl1_obs', Mcl1())
Observable('CytoCA_obs', CytoCA())
Observable('CytoCC_obs', CytoCC())
Observable('BakA_obs', BakA())
Observable('BaxC_obs', BaxC())
Observable('BaxA_obs', BaxA())
Observable('ApafI_obs', ApafI())
Observable('Bcl2_obs', Bcl2())
Observable('BidU_obs', BidU())
Observable('BidT_obs', BidT())
Observable('C3A_obs', C3A())
Observable('flip_obs', flip())
Observable('ApafA_obs', ApafA())
Observable('BidM_obs', BidM())
Observable('BakM_obs', BakM())
Observable('C6A_obs', C6A())
Observable('BclxLC_obs', BclxLC())
Observable('CytoCM_obs', CytoCM())

Rule('dimerization_0_L_subunit_a_R_subunit_b_DISC_dimer', L(R=None) + R(L=None) | L(R=1) % R(L=1), dimerization_0_L_subunit_a_R_subunit_b_DISC_dimer_2kf_0, dimerization_0_L_subunit_a_R_subunit_b_DISC_dimer_1kr_0)
Rule('dimerization_1_L_subunit_a_R_subunit_b_DISC_dimer', L(R=1) % R(L=1) >> DISC(C8pro=None, flip=None), dimerization_1_L_subunit_a_R_subunit_b_DISC_dimer_1kf_0)
Rule('catalysis_0_DISC_catalyzer_C8pro_substrate_C8A_product', DISC(C8pro=None, flip=None) + C8pro(DISC=None, C6A=None) | DISC(C8pro=1, flip=None) % C8pro(DISC=1, C6A=None), catalysis_0_DISC_catalyzer_C8pro_substrate_C8A_product_2kf_0, catalysis_0_DISC_catalyzer_C8pro_substrate_C8A_product_1kr_0)
Rule('catalysis_1_DISC_catalyzer_C8pro_substrate_C8A_product', DISC(C8pro=1, flip=None) % C8pro(DISC=1, C6A=None) >> DISC(C8pro=None, flip=None) + C8A(BidU=None, BAR=None, C3pro=None), catalysis_1_DISC_catalyzer_C8pro_substrate_C8A_product_1kc_0)
Rule('catalysis_0_C8A_catalyzer_BidU_substrate_BidT_product', C8A(BidU=None, BAR=None, C3pro=None) + BidU(C8A=None) | C8A(BidU=1, BAR=None, C3pro=None) % BidU(C8A=1), catalysis_0_C8A_catalyzer_BidU_substrate_BidT_product_2kf_0, catalysis_0_C8A_catalyzer_BidU_substrate_BidT_product_1kr_0)
Rule('catalysis_1_C8A_catalyzer_BidU_substrate_BidT_product', C8A(BidU=1, BAR=None, C3pro=None) % BidU(C8A=1) >> C8A(BidU=None, BAR=None, C3pro=None) + BidT(), catalysis_1_C8A_catalyzer_BidU_substrate_BidT_product_1kc_0)
Rule('inhibition_0_flip_inhibitor_DISC_inh_target', flip(DISC=None) + DISC(C8pro=None, flip=None) | flip(DISC=1) % DISC(C8pro=None, flip=1), inhibition_0_flip_inhibitor_DISC_inh_target_2kf_0, inhibition_0_flip_inhibitor_DISC_inh_target_1kr_0)
Rule('inhibition_0_BAR_inhibitor_C8A_inh_target', BAR(C8A=None) + C8A(BidU=None, BAR=None, C3pro=None) | BAR(C8A=1) % C8A(BidU=None, BAR=1, C3pro=None), inhibition_0_BAR_inhibitor_C8A_inh_target_2kf_0, inhibition_0_BAR_inhibitor_C8A_inh_target_1kr_0)
Rule('equilibration_0_SmacC_equil_a_SmacA_equil_b', SmacC() | SmacA(XIAP=None), equilibration_0_SmacC_equil_a_SmacA_equil_b_1kf_0, equilibration_0_SmacC_equil_a_SmacA_equil_b_1kr_0)
Rule('equilibration_0_CytoCC_equil_a_CytoCA_equil_b', CytoCC() | CytoCA(ApafI=None), equilibration_0_CytoCC_equil_a_CytoCA_equil_b_1kf_0, equilibration_0_CytoCC_equil_a_CytoCA_equil_b_1kr_0)
Rule('catalysis_0_CytoCA_catalyzer_ApafI_substrate_ApafA_product', CytoCA(ApafI=None) + ApafI(CytoCA=None) | CytoCA(ApafI=1) % ApafI(CytoCA=1), catalysis_0_CytoCA_catalyzer_ApafI_substrate_ApafA_product_2kf_0, catalysis_0_CytoCA_catalyzer_ApafI_substrate_ApafA_product_1kr_0)
Rule('catalysis_1_CytoCA_catalyzer_ApafI_substrate_ApafA_product', CytoCA(ApafI=1) % ApafI(CytoCA=1) >> CytoCA(ApafI=None) + ApafA(), catalysis_1_CytoCA_catalyzer_ApafI_substrate_ApafA_product_1kc_0)
Rule('conversion_0_C9_subunit_d_ApafA_subunit_c_Apop_complex', ApafA() + C9() | Apop(C3pro=None, XIAP=None), conversion_0_C9_subunit_d_ApafA_subunit_c_Apop_complex_2kf_0, conversion_0_C9_subunit_d_ApafA_subunit_c_Apop_complex_1kr_0)
Rule('catalysis_0_Apop_catalyzer_C3pro_substrate_C3A_product', Apop(C3pro=None, XIAP=None) + C3pro(Apop=None, C8A=None) | Apop(C3pro=1, XIAP=None) % C3pro(Apop=1, C8A=None), catalysis_0_Apop_catalyzer_C3pro_substrate_C3A_product_2kf_0, catalysis_0_Apop_catalyzer_C3pro_substrate_C3A_product_1kr_0)
Rule('catalysis_1_Apop_catalyzer_C3pro_substrate_C3A_product', Apop(C3pro=1, XIAP=None) % C3pro(Apop=1, C8A=None) >> Apop(C3pro=None, XIAP=None) + C3A(XIAP=None, PARPU=None, C6pro=None), catalysis_1_Apop_catalyzer_C3pro_substrate_C3A_product_1kc_0)
Rule('inhibition_0_XIAP_inhibitor_Apop_inh_target', XIAP(Apop=None, SmacA=None, C3A=None) + Apop(C3pro=None, XIAP=None) | XIAP(Apop=1, SmacA=None, C3A=None) % Apop(C3pro=None, XIAP=1), inhibition_0_XIAP_inhibitor_Apop_inh_target_2kf_0, inhibition_0_XIAP_inhibitor_Apop_inh_target_1kr_0)
Rule('inhibition_0_SmacA_inhibitor_XIAP_inh_target', SmacA(XIAP=None) + XIAP(Apop=None, SmacA=None, C3A=None) | SmacA(XIAP=1) % XIAP(Apop=None, SmacA=1, C3A=None), inhibition_0_SmacA_inhibitor_XIAP_inh_target_2kf_0, inhibition_0_SmacA_inhibitor_XIAP_inh_target_1kr_0)
Rule('catalysis_0_C8A_catalyzer_C3pro_substrate_C3A_product', C8A(BidU=None, BAR=None, C3pro=None) + C3pro(Apop=None, C8A=None) | C8A(BidU=None, BAR=None, C3pro=1) % C3pro(Apop=None, C8A=1), catalysis_0_C8A_catalyzer_C3pro_substrate_C3A_product_2kf_0, catalysis_0_C8A_catalyzer_C3pro_substrate_C3A_product_1kr_0)
Rule('catalysis_1_C8A_catalyzer_C3pro_substrate_C3A_product', C8A(BidU=None, BAR=None, C3pro=1) % C3pro(Apop=None, C8A=1) >> C8A(BidU=None, BAR=None, C3pro=None) + C3A(XIAP=None, PARPU=None, C6pro=None), catalysis_1_C8A_catalyzer_C3pro_substrate_C3A_product_1kc_0)
Rule('catalysis_0_XIAP_catalyzer_C3A_substrate_C3ub_product', XIAP(Apop=None, SmacA=None, C3A=None) + C3A(XIAP=None, PARPU=None, C6pro=None) | XIAP(Apop=None, SmacA=None, C3A=1) % C3A(XIAP=1, PARPU=None, C6pro=None), catalysis_0_XIAP_catalyzer_C3A_substrate_C3ub_product_2kf_0, catalysis_0_XIAP_catalyzer_C3A_substrate_C3ub_product_1kr_0)
Rule('catalysis_1_XIAP_catalyzer_C3A_substrate_C3ub_product', XIAP(Apop=None, SmacA=None, C3A=1) % C3A(XIAP=1, PARPU=None, C6pro=None) >> XIAP(Apop=None, SmacA=None, C3A=None) + C3ub(), catalysis_1_XIAP_catalyzer_C3A_substrate_C3ub_product_1kc_0)
Rule('catalysis_0_C3A_catalyzer_PARPU_substrate_PARPC_product', C3A(XIAP=None, PARPU=None, C6pro=None) + PARPU(C3A=None) | C3A(XIAP=None, PARPU=1, C6pro=None) % PARPU(C3A=1), catalysis_0_C3A_catalyzer_PARPU_substrate_PARPC_product_2kf_0, catalysis_0_C3A_catalyzer_PARPU_substrate_PARPC_product_1kr_0)
Rule('catalysis_1_C3A_catalyzer_PARPU_substrate_PARPC_product', C3A(XIAP=None, PARPU=1, C6pro=None) % PARPU(C3A=1) >> C3A(XIAP=None, PARPU=None, C6pro=None) + PARPC(), catalysis_1_C3A_catalyzer_PARPU_substrate_PARPC_product_1kc_0)
Rule('catalysis_0_C3A_catalyzer_C6pro_substrate_C6A_product', C3A(XIAP=None, PARPU=None, C6pro=None) + C6pro(C3A=None) | C3A(XIAP=None, PARPU=None, C6pro=1) % C6pro(C3A=1), catalysis_0_C3A_catalyzer_C6pro_substrate_C6A_product_2kf_0, catalysis_0_C3A_catalyzer_C6pro_substrate_C6A_product_1kr_0)
Rule('catalysis_1_C3A_catalyzer_C6pro_substrate_C6A_product', C3A(XIAP=None, PARPU=None, C6pro=1) % C6pro(C3A=1) >> C3A(XIAP=None, PARPU=None, C6pro=None) + C6A(C8pro=None), catalysis_1_C3A_catalyzer_C6pro_substrate_C6A_product_1kc_0)
Rule('catalysis_0_C6A_catalyzer_C8pro_substrate_C8A_product', C6A(C8pro=None) + C8pro(DISC=None, C6A=None) | C6A(C8pro=1) % C8pro(DISC=None, C6A=1), catalysis_0_C6A_catalyzer_C8pro_substrate_C8A_product_2kf_0, catalysis_0_C6A_catalyzer_C8pro_substrate_C8A_product_1kr_0)
Rule('catalysis_1_C6A_catalyzer_C8pro_substrate_C8A_product', C6A(C8pro=1) % C8pro(DISC=None, C6A=1) >> C6A(C8pro=None) + C8A(BidU=None, BAR=None, C3pro=None), catalysis_1_C6A_catalyzer_C8pro_substrate_C8A_product_1kc_0)
Rule('equilibration_0_BidT_equil_a_BidM_equil_b', BidT() | BidM(BaxM=None, BakM=None, Bcl2=None, BclxLM=None, Mcl1=None), equilibration_0_BidT_equil_a_BidM_equil_b_1kf_0, equilibration_0_BidT_equil_a_BidM_equil_b_1kr_0)
Rule('equilibration_0_BaxC_equil_a_BaxM_equil_b', BaxC() | BaxM(BidM=None, BaxA=None), equilibration_0_BaxC_equil_a_BaxM_equil_b_1kf_0, equilibration_0_BaxC_equil_a_BaxM_equil_b_1kr_0)
Rule('equilibration_0_BclxLC_equil_a_BclxLM_equil_b', BclxLC() | BclxLM(BidM=None, BaxA=None, BakA=None, Bad=None), equilibration_0_BclxLC_equil_a_BclxLM_equil_b_1kf_0, equilibration_0_BclxLC_equil_a_BclxLM_equil_b_1kr_0)
Rule('catalysis_0_BidM_catalyzer_BaxM_substrate_BaxA_product', BidM(BaxM=None, BakM=None, Bcl2=None, BclxLM=None, Mcl1=None) + BaxM(BidM=None, BaxA=None) | BidM(BaxM=1, BakM=None, Bcl2=None, BclxLM=None, Mcl1=None) % BaxM(BidM=1, BaxA=None), catalysis_0_BidM_catalyzer_BaxM_substrate_BaxA_product_2kf_0, catalysis_0_BidM_catalyzer_BaxM_substrate_BaxA_product_1kr_0)
Rule('catalysis_1_BidM_catalyzer_BaxM_substrate_BaxA_product', BidM(BaxM=1, BakM=None, Bcl2=None, BclxLM=None, Mcl1=None) % BaxM(BidM=1, BaxA=None) >> BidM(BaxM=None, BakM=None, Bcl2=None, BclxLM=None, Mcl1=None) + BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=None, BaxA_2=None, CytoCM=None, SmacM=None), catalysis_1_BidM_catalyzer_BaxM_substrate_BaxA_product_1kc_0)
Rule('catalysis_0_BidM_catalyzer_BakM_substrate_BakA_product', BidM(BaxM=None, BakM=None, Bcl2=None, BclxLM=None, Mcl1=None) + BakM(BidM=None, BakA=None) | BidM(BaxM=None, BakM=1, Bcl2=None, BclxLM=None, Mcl1=None) % BakM(BidM=1, BakA=None), catalysis_0_BidM_catalyzer_BakM_substrate_BakA_product_2kf_0, catalysis_0_BidM_catalyzer_BakM_substrate_BakA_product_1kr_0)
Rule('catalysis_1_BidM_catalyzer_BakM_substrate_BakA_product', BidM(BaxM=None, BakM=1, Bcl2=None, BclxLM=None, Mcl1=None) % BakM(BidM=1, BakA=None) >> BidM(BaxM=None, BakM=None, Bcl2=None, BclxLM=None, Mcl1=None) + BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=None, BakA_2=None, CytoCM=None, SmacM=None), catalysis_1_BidM_catalyzer_BakM_substrate_BakA_product_1kc_0)
Rule('self_catalyze_0_BaxA_self_catalyzer_BaxM_self_substrate', BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=None, BaxA_2=None, CytoCM=None, SmacM=None) + BaxM(BidM=None, BaxA=None) | BaxA(BaxM=1, Bcl2=None, BclxLM=None, BaxA_1=None, BaxA_2=None, CytoCM=None, SmacM=None) % BaxM(BidM=None, BaxA=1), self_catalyze_0_BaxA_self_catalyzer_BaxM_self_substrate_2kf_0, self_catalyze_0_BaxA_self_catalyzer_BaxM_self_substrate_1kr_0)
Rule('self_catalyze_1_BaxA_self_catalyzer_BaxM_self_substrate', BaxA(BaxM=1, Bcl2=None, BclxLM=None, BaxA_1=None, BaxA_2=None, CytoCM=None, SmacM=None) % BaxM(BidM=None, BaxA=1) >> BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=None, BaxA_2=None, CytoCM=None, SmacM=None) + BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=None, BaxA_2=None, CytoCM=None, SmacM=None), self_catalyze_1_BaxA_self_catalyzer_BaxM_self_substrate_1kc_0)
Rule('self_catalyze_0_BakA_self_catalyzer_BakM_self_substrate', BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=None, BakA_2=None, CytoCM=None, SmacM=None) + BakM(BidM=None, BakA=None) | BakA(BakM=1, BclxLM=None, Mcl1=None, BakA_1=None, BakA_2=None, CytoCM=None, SmacM=None) % BakM(BidM=None, BakA=1), self_catalyze_0_BakA_self_catalyzer_BakM_self_substrate_2kf_0, self_catalyze_0_BakA_self_catalyzer_BakM_self_substrate_1kr_0)
Rule('self_catalyze_1_BakA_self_catalyzer_BakM_self_substrate', BakA(BakM=1, BclxLM=None, Mcl1=None, BakA_1=None, BakA_2=None, CytoCM=None, SmacM=None) % BakM(BidM=None, BakA=1) >> BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=None, BakA_2=None, CytoCM=None, SmacM=None) + BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=None, BakA_2=None, CytoCM=None, SmacM=None), self_catalyze_1_BakA_self_catalyzer_BakM_self_substrate_1kc_0)
Rule('inhibition_0_Bcl2_inhibitor_BidM_inh_target', Bcl2(BidM=None, BaxA=None, Bad=None) + BidM(BaxM=None, BakM=None, Bcl2=None, BclxLM=None, Mcl1=None) | Bcl2(BidM=1, BaxA=None, Bad=None) % BidM(BaxM=None, BakM=None, Bcl2=1, BclxLM=None, Mcl1=None), inhibition_0_Bcl2_inhibitor_BidM_inh_target_2kf_0, inhibition_0_Bcl2_inhibitor_BidM_inh_target_1kr_0)
Rule('inhibition_0_BclxLM_inhibitor_BidM_inh_target', BclxLM(BidM=None, BaxA=None, BakA=None, Bad=None) + BidM(BaxM=None, BakM=None, Bcl2=None, BclxLM=None, Mcl1=None) | BclxLM(BidM=1, BaxA=None, BakA=None, Bad=None) % BidM(BaxM=None, BakM=None, Bcl2=None, BclxLM=1, Mcl1=None), inhibition_0_BclxLM_inhibitor_BidM_inh_target_2kf_0, inhibition_0_BclxLM_inhibitor_BidM_inh_target_1kr_0)
Rule('inhibition_0_Mcl1_inhibitor_BidM_inh_target', Mcl1(BidM=None, BakA=None, Noxa=None) + BidM(BaxM=None, BakM=None, Bcl2=None, BclxLM=None, Mcl1=None) | Mcl1(BidM=1, BakA=None, Noxa=None) % BidM(BaxM=None, BakM=None, Bcl2=None, BclxLM=None, Mcl1=1), inhibition_0_Mcl1_inhibitor_BidM_inh_target_2kf_0, inhibition_0_Mcl1_inhibitor_BidM_inh_target_1kr_0)
Rule('inhibition_0_Bcl2_inhibitor_BaxA_inh_target', Bcl2(BidM=None, BaxA=None, Bad=None) + BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=None, BaxA_2=None, CytoCM=None, SmacM=None) | Bcl2(BidM=None, BaxA=1, Bad=None) % BaxA(BaxM=None, Bcl2=1, BclxLM=None, BaxA_1=None, BaxA_2=None, CytoCM=None, SmacM=None), inhibition_0_Bcl2_inhibitor_BaxA_inh_target_2kf_0, inhibition_0_Bcl2_inhibitor_BaxA_inh_target_1kr_0)
Rule('inhibition_0_BclxLM_inhibitor_BaxA_inh_target', BclxLM(BidM=None, BaxA=None, BakA=None, Bad=None) + BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=None, BaxA_2=None, CytoCM=None, SmacM=None) | BclxLM(BidM=None, BaxA=1, BakA=None, Bad=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=1, BaxA_1=None, BaxA_2=None, CytoCM=None, SmacM=None), inhibition_0_BclxLM_inhibitor_BaxA_inh_target_2kf_0, inhibition_0_BclxLM_inhibitor_BaxA_inh_target_1kr_0)
Rule('inhibition_0_BclxLM_inhibitor_BakA_inh_target', BclxLM(BidM=None, BaxA=None, BakA=None, Bad=None) + BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=None, BakA_2=None, CytoCM=None, SmacM=None) | BclxLM(BidM=None, BaxA=None, BakA=1, Bad=None) % BakA(BakM=None, BclxLM=1, Mcl1=None, BakA_1=None, BakA_2=None, CytoCM=None, SmacM=None), inhibition_0_BclxLM_inhibitor_BakA_inh_target_2kf_0, inhibition_0_BclxLM_inhibitor_BakA_inh_target_1kr_0)
Rule('inhibition_0_Mcl1_inhibitor_BakA_inh_target', Mcl1(BidM=None, BakA=None, Noxa=None) + BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=None, BakA_2=None, CytoCM=None, SmacM=None) | Mcl1(BidM=None, BakA=1, Noxa=None) % BakA(BakM=None, BclxLM=None, Mcl1=1, BakA_1=None, BakA_2=None, CytoCM=None, SmacM=None), inhibition_0_Mcl1_inhibitor_BakA_inh_target_2kf_0, inhibition_0_Mcl1_inhibitor_BakA_inh_target_1kr_0)
Rule('inhibition_0_Bad_inhibitor_Bcl2_inh_target', Bad(Bcl2=None, BclxLM=None) + Bcl2(BidM=None, BaxA=None, Bad=None) | Bad(Bcl2=1, BclxLM=None) % Bcl2(BidM=None, BaxA=None, Bad=1), inhibition_0_Bad_inhibitor_Bcl2_inh_target_2kf_0, inhibition_0_Bad_inhibitor_Bcl2_inh_target_1kr_0)
Rule('inhibition_0_Bad_inhibitor_BclxLM_inh_target', Bad(Bcl2=None, BclxLM=None) + BclxLM(BidM=None, BaxA=None, BakA=None, Bad=None) | Bad(Bcl2=None, BclxLM=1) % BclxLM(BidM=None, BaxA=None, BakA=None, Bad=1), inhibition_0_Bad_inhibitor_BclxLM_inh_target_2kf_0, inhibition_0_Bad_inhibitor_BclxLM_inh_target_1kr_0)
Rule('inhibition_0_Noxa_inhibitor_Mcl1_inh_target', Noxa(Mcl1=None) + Mcl1(BidM=None, BakA=None, Noxa=None) | Noxa(Mcl1=1) % Mcl1(BidM=None, BakA=None, Noxa=1), inhibition_0_Noxa_inhibitor_Mcl1_inh_target_2kf_0, inhibition_0_Noxa_inhibitor_Mcl1_inh_target_1kr_0)
Rule('pore_formation_0_BaxA_pore', BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=None, BaxA_2=None, CytoCM=None, SmacM=None) + BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=None, BaxA_2=None, CytoCM=None, SmacM=None) | BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=None, BaxA_2=1, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=1, BaxA_2=None, CytoCM=None, SmacM=None), pore_formation_0_BaxA_pore_2kf_0, pore_formation_0_BaxA_pore_1kr_0)
Rule('pore_formation_1_BaxA_pore', BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=None, BaxA_2=None, CytoCM=None, SmacM=None) + BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=None, BaxA_2=1, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=1, BaxA_2=None, CytoCM=None, SmacM=None) | BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=3, BaxA_2=1, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=1, BaxA_2=2, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=2, BaxA_2=3, CytoCM=None, SmacM=None), pore_formation_1_BaxA_pore_2kf_0, pore_formation_1_BaxA_pore_1kr_0)
Rule('pore_formation_2_BaxA_pore', BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=None, BaxA_2=None, CytoCM=None, SmacM=None) + BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=3, BaxA_2=1, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=1, BaxA_2=2, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=2, BaxA_2=3, CytoCM=None, SmacM=None) | BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=4, BaxA_2=1, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=1, BaxA_2=2, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=2, BaxA_2=3, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=3, BaxA_2=4, CytoCM=None, SmacM=None), pore_formation_2_BaxA_pore_2kf_0, pore_formation_2_BaxA_pore_1kr_0)
Rule('pore_formation_0_BakA_pore', BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=None, BakA_2=None, CytoCM=None, SmacM=None) + BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=None, BakA_2=None, CytoCM=None, SmacM=None) | BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=None, BakA_2=1, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=1, BakA_2=None, CytoCM=None, SmacM=None), pore_formation_0_BakA_pore_2kf_0, pore_formation_0_BakA_pore_1kr_0)
Rule('pore_formation_1_BakA_pore', BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=None, BakA_2=None, CytoCM=None, SmacM=None) + BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=None, BakA_2=1, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=1, BakA_2=None, CytoCM=None, SmacM=None) | BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=3, BakA_2=1, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=1, BakA_2=2, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=2, BakA_2=3, CytoCM=None, SmacM=None), pore_formation_1_BakA_pore_2kf_0, pore_formation_1_BakA_pore_1kr_0)
Rule('pore_formation_2_BakA_pore', BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=None, BakA_2=None, CytoCM=None, SmacM=None) + BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=3, BakA_2=1, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=1, BakA_2=2, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=2, BakA_2=3, CytoCM=None, SmacM=None) | BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=4, BakA_2=1, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=1, BakA_2=2, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=2, BakA_2=3, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=3, BakA_2=4, CytoCM=None, SmacM=None), pore_formation_2_BakA_pore_2kf_0, pore_formation_2_BakA_pore_1kr_0)
Rule('transport_0_BaxA_pore_CytoCM_cargo_M_CytoCC_cargo_C', BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=4, BaxA_2=1, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=1, BaxA_2=2, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=2, BaxA_2=3, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=3, BaxA_2=4, CytoCM=None, SmacM=None) + CytoCM(BaxA=None, BakA=None) | BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=4, BaxA_2=1, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=1, BaxA_2=2, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=2, BaxA_2=3, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=3, BaxA_2=4, CytoCM=5, SmacM=None) % CytoCM(BaxA=5, BakA=None), transport_0_BaxA_pore_CytoCM_cargo_M_CytoCC_cargo_C_2kf_0, transport_0_BaxA_pore_CytoCM_cargo_M_CytoCC_cargo_C_1kr_0)
Rule('transport_1_BaxA_pore_CytoCM_cargo_M_CytoCC_cargo_C', BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=4, BaxA_2=1, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=1, BaxA_2=2, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=2, BaxA_2=3, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=3, BaxA_2=4, CytoCM=5, SmacM=None) % CytoCM(BaxA=5, BakA=None) >> BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=4, BaxA_2=1, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=1, BaxA_2=2, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=2, BaxA_2=3, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=3, BaxA_2=4, CytoCM=None, SmacM=None) + CytoCC(), transport_1_BaxA_pore_CytoCM_cargo_M_CytoCC_cargo_C_1kc_0)
Rule('transport_0_BaxA_pore_SmacM_cargo_M_SmacC_cargo_C', BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=4, BaxA_2=1, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=1, BaxA_2=2, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=2, BaxA_2=3, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=3, BaxA_2=4, CytoCM=None, SmacM=None) + SmacM(BaxA=None, BakA=None) | BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=4, BaxA_2=1, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=1, BaxA_2=2, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=2, BaxA_2=3, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=3, BaxA_2=4, CytoCM=None, SmacM=5) % SmacM(BaxA=5, BakA=None), transport_0_BaxA_pore_SmacM_cargo_M_SmacC_cargo_C_2kf_0, transport_0_BaxA_pore_SmacM_cargo_M_SmacC_cargo_C_1kr_0)
Rule('transport_1_BaxA_pore_SmacM_cargo_M_SmacC_cargo_C', BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=4, BaxA_2=1, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=1, BaxA_2=2, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=2, BaxA_2=3, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=3, BaxA_2=4, CytoCM=None, SmacM=5) % SmacM(BaxA=5, BakA=None) >> BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=4, BaxA_2=1, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=1, BaxA_2=2, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=2, BaxA_2=3, CytoCM=None, SmacM=None) % BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=3, BaxA_2=4, CytoCM=None, SmacM=None) + SmacC(), transport_1_BaxA_pore_SmacM_cargo_M_SmacC_cargo_C_1kc_0)
Rule('transport_0_BakA_pore_CytoCM_cargo_M_CytoCC_cargo_C', BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=4, BakA_2=1, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=1, BakA_2=2, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=2, BakA_2=3, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=3, BakA_2=4, CytoCM=None, SmacM=None) + CytoCM(BaxA=None, BakA=None) | BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=4, BakA_2=1, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=1, BakA_2=2, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=2, BakA_2=3, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=3, BakA_2=4, CytoCM=5, SmacM=None) % CytoCM(BaxA=None, BakA=5), transport_0_BakA_pore_CytoCM_cargo_M_CytoCC_cargo_C_2kf_0, transport_0_BakA_pore_CytoCM_cargo_M_CytoCC_cargo_C_1kr_0)
Rule('transport_1_BakA_pore_CytoCM_cargo_M_CytoCC_cargo_C', BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=4, BakA_2=1, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=1, BakA_2=2, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=2, BakA_2=3, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=3, BakA_2=4, CytoCM=5, SmacM=None) % CytoCM(BaxA=None, BakA=5) >> BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=4, BakA_2=1, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=1, BakA_2=2, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=2, BakA_2=3, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=3, BakA_2=4, CytoCM=None, SmacM=None) + CytoCC(), transport_1_BakA_pore_CytoCM_cargo_M_CytoCC_cargo_C_1kc_0)
Rule('transport_0_BakA_pore_SmacM_cargo_M_SmacC_cargo_C', BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=4, BakA_2=1, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=1, BakA_2=2, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=2, BakA_2=3, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=3, BakA_2=4, CytoCM=None, SmacM=None) + SmacM(BaxA=None, BakA=None) | BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=4, BakA_2=1, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=1, BakA_2=2, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=2, BakA_2=3, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=3, BakA_2=4, CytoCM=None, SmacM=5) % SmacM(BaxA=None, BakA=5), transport_0_BakA_pore_SmacM_cargo_M_SmacC_cargo_C_2kf_0, transport_0_BakA_pore_SmacM_cargo_M_SmacC_cargo_C_1kr_0)
Rule('transport_1_BakA_pore_SmacM_cargo_M_SmacC_cargo_C', BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=4, BakA_2=1, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=1, BakA_2=2, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=2, BakA_2=3, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=3, BakA_2=4, CytoCM=None, SmacM=5) % SmacM(BaxA=None, BakA=5) >> BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=4, BakA_2=1, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=1, BakA_2=2, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=2, BakA_2=3, CytoCM=None, SmacM=None) % BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=3, BakA_2=4, CytoCM=None, SmacM=None) + SmacC(), transport_1_BakA_pore_SmacM_cargo_M_SmacC_cargo_C_1kc_0)

Initial(Noxa(Mcl1=None), Noxa_0)
Initial(BAR(C8A=None), BAR_0)
Initial(BclxLM(BidM=None, BaxA=None, BakA=None, Bad=None), BclxLM_0)
Initial(BaxM(BidM=None, BaxA=None), BaxM_0)
Initial(C8A(BidU=None, BAR=None, C3pro=None), C8A_0)
Initial(XIAP(Apop=None, SmacA=None, C3A=None), XIAP_0)
Initial(DISC(C8pro=None, flip=None), DISC_0)
Initial(SmacM(BaxA=None, BakA=None), SmacM_0)
Initial(C6pro(C3A=None), C6pro_0)
Initial(Apop(C3pro=None, XIAP=None), Apop_0)
Initial(SmacA(XIAP=None), SmacA_0)
Initial(SmacC(), SmacC_0)
Initial(PARPU(C3A=None), PARPU_0)
Initial(C9(), C9_0)
Initial(Bad(Bcl2=None, BclxLM=None), Bad_0)
Initial(C3ub(), C3ub_0)
Initial(C8pro(DISC=None, C6A=None), C8pro_0)
Initial(PARPC(), PARPC_0)
Initial(L(R=None), L_0)
Initial(C3pro(Apop=None, C8A=None), C3pro_0)
Initial(R(L=None), R_0)
Initial(Mcl1(BidM=None, BakA=None, Noxa=None), Mcl1_0)
Initial(CytoCA(ApafI=None), CytoCA_0)
Initial(CytoCC(), CytoCC_0)
Initial(BakA(BakM=None, BclxLM=None, Mcl1=None, BakA_1=None, BakA_2=None, CytoCM=None, SmacM=None), BakA_0)
Initial(BaxC(), BaxC_0)
Initial(BaxA(BaxM=None, Bcl2=None, BclxLM=None, BaxA_1=None, BaxA_2=None, CytoCM=None, SmacM=None), BaxA_0)
Initial(ApafI(CytoCA=None), ApafI_0)
Initial(Bcl2(BidM=None, BaxA=None, Bad=None), Bcl2_0)
Initial(BidU(C8A=None), BidU_0)
Initial(BidT(), BidT_0)
Initial(C3A(XIAP=None, PARPU=None, C6pro=None), C3A_0)
Initial(flip(DISC=None), flip_0)
Initial(ApafA(), ApafA_0)
Initial(BidM(BaxM=None, BakM=None, Bcl2=None, BclxLM=None, Mcl1=None), BidM_0)
Initial(BakM(BidM=None, BakA=None), BakM_0)
Initial(C6A(C8pro=None), C6A_0)
Initial(BclxLC(), BclxLC_0)
Initial(CytoCM(BaxA=None, BakA=None), CytoCM_0)


