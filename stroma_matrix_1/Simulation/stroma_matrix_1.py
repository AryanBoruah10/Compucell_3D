
from cc3d import CompuCellSetup
        


from stroma_matrix_1Steppables import ConstraintInitializerSteppable

CompuCellSetup.register_steppable(steppable=ConstraintInitializerSteppable(frequency=1))




# from stroma_matrix_1Steppables import GrowthSteppable

# CompuCellSetup.register_steppable(steppable=GrowthSteppable(frequency=1))




from stroma_matrix_1Steppables import MitosisSteppable

CompuCellSetup.register_steppable(steppable=MitosisSteppable(frequency=1))


CompuCellSetup.run()
