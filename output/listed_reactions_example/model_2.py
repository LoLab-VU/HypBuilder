# exported from PySB model 'model'

from pysb import Model, Monomer, Parameter, Expression, Compartment, Rule, Observable, Initial, MatchOnce, Annotation, MultiState, Tag, ANY, WILD


Model()

Monomer('A', ['B', 'C', 'E', 'F'])
Monomer('B', ['A'])
Monomer('C', ['A'])
Monomer('D')
Monomer('E', ['A'])
Monomer('F', ['A'])
Monomer('G')

Parameter('catalysis_0_A_catalyzer_B_substrate_C_product_2kf', 1.0)
Parameter('catalysis_0_A_catalyzer_B_substrate_C_product_1kr', 1.0)
Parameter('catalysis_1_A_catalyzer_B_substrate_C_product_1kc', 1.0)
Parameter('catalysis_0_A_catalyzer_C_substrate_D_product_2kf', 1.0)
Parameter('catalysis_0_A_catalyzer_C_substrate_D_product_1kr', 1.0)
Parameter('catalysis_1_A_catalyzer_C_substrate_D_product_1kc', 1.0)
Parameter('catalysis_0_A_catalyzer_E_substrate_F_product_2kf', 1.0)
Parameter('catalysis_0_A_catalyzer_E_substrate_F_product_1kr', 1.0)
Parameter('catalysis_1_A_catalyzer_E_substrate_F_product_1kc', 1.0)
Parameter('catalysis_0_A_catalyzer_F_substrate_G_product_2kf', 1.0)
Parameter('catalysis_0_A_catalyzer_F_substrate_G_product_1kr', 1.0)
Parameter('catalysis_1_A_catalyzer_F_substrate_G_product_1kc', 1.0)
Parameter('A_0', 1.0)
Parameter('B_0', 1.0)
Parameter('C_0', 1.0)
Parameter('D_0', 1.0)
Parameter('E_0', 1.0)
Parameter('F_0', 1.0)
Parameter('G_0', 1.0)

Observable('A_obs', A())
Observable('B_obs', B())
Observable('C_obs', C())
Observable('D_obs', D())
Observable('E_obs', E())
Observable('F_obs', F())
Observable('G_obs', G())

Rule('catalysis_0_A_catalyzer_B_substrate_C_product', A(B=None, C=None, E=None, F=None) + B(A=None) | A(B=1, C=None, E=None, F=None) % B(A=1), catalysis_0_A_catalyzer_B_substrate_C_product_2kf, catalysis_0_A_catalyzer_B_substrate_C_product_1kr)
Rule('catalysis_1_A_catalyzer_B_substrate_C_product', A(B=1, C=None, E=None, F=None) % B(A=1) >> A(B=None, C=None, E=None, F=None) + C(A=None), catalysis_1_A_catalyzer_B_substrate_C_product_1kc)
Rule('catalysis_0_A_catalyzer_C_substrate_D_product', A(B=None, C=None, E=None, F=None) + C(A=None) | A(B=None, C=1, E=None, F=None) % C(A=1), catalysis_0_A_catalyzer_C_substrate_D_product_2kf, catalysis_0_A_catalyzer_C_substrate_D_product_1kr)
Rule('catalysis_1_A_catalyzer_C_substrate_D_product', A(B=None, C=1, E=None, F=None) % C(A=1) >> A(B=None, C=None, E=None, F=None) + D(), catalysis_1_A_catalyzer_C_substrate_D_product_1kc)
Rule('catalysis_0_A_catalyzer_E_substrate_F_product', A(B=None, C=None, E=None, F=None) + E(A=None) | A(B=None, C=None, E=1, F=None) % E(A=1), catalysis_0_A_catalyzer_E_substrate_F_product_2kf, catalysis_0_A_catalyzer_E_substrate_F_product_1kr)
Rule('catalysis_1_A_catalyzer_E_substrate_F_product', A(B=None, C=None, E=1, F=None) % E(A=1) >> A(B=None, C=None, E=None, F=None) + F(A=None), catalysis_1_A_catalyzer_E_substrate_F_product_1kc)
Rule('catalysis_0_A_catalyzer_F_substrate_G_product', A(B=None, C=None, E=None, F=None) + F(A=None) | A(B=None, C=None, E=None, F=1) % F(A=1), catalysis_0_A_catalyzer_F_substrate_G_product_2kf, catalysis_0_A_catalyzer_F_substrate_G_product_1kr)
Rule('catalysis_1_A_catalyzer_F_substrate_G_product', A(B=None, C=None, E=None, F=1) % F(A=1) >> A(B=None, C=None, E=None, F=None) + G(), catalysis_1_A_catalyzer_F_substrate_G_product_1kc)

Initial(A(B=None, C=None, E=None, F=None), A_0)
Initial(B(A=None), B_0)
Initial(C(A=None), C_0)
Initial(D(), D_0)
Initial(E(A=None), E_0)
Initial(F(A=None), F_0)
Initial(G(), G_0)

