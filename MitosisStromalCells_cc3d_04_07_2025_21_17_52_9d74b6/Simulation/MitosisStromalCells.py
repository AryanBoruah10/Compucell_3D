
from cc3d import CompuCellSetup
        


from MitosisStromalCellsSteppables import ConstraintInitializerSteppable

CompuCellSetup.register_steppable(steppable=ConstraintInitializerSteppable(frequency=1))




# from MitosisStromalCellsSteppables import GrowthSteppable

# CompuCellSetup.register_steppable(steppable=GrowthSteppable(frequency=1))
# from MitosisStromalCellsSteppables import PurpleCellGravitySteppable
# CompuCellSetup.register_steppable(steppable=PurpleCellGravitySteppable(frequency=1))



from MitosisStromalCellsSteppables import MitosisSteppable

CompuCellSetup.register_steppable(steppable=MitosisSteppable(frequency=1))


CompuCellSetup.run()

