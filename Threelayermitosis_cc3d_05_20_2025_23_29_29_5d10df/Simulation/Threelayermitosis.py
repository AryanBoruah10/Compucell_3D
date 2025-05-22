
from cc3d import CompuCellSetup
        

# from ThreelayermitosisSteppables import ThreelayermitosisSteppable

# CompuCellSetup.register_steppable(steppable=ThreelayermitosisSteppable(frequency=1))
from ThreelayermitosisSteppables import ThreelayermitosisSteppable
tls = ThreelayermitosisSteppable(frequency=1)
tls.add_cell_type_parameters(cell_type=1, count=80, target_volume=25, lambda_volume=10.0)
tls.add_cell_type_parameters(cell_type=5, count=0, target_volume=5.0, lambda_volume=2.0)
tls.set_fraction_of_water(0.25)

CompuCellSetup.register_steppable(steppable=tls)
# from ThreelayermitosisSteppables import ConstraintInitializerSteppable

# CompuCellSetup.register_steppable(steppable=ConstraintInitializerSteppable(frequency=1))

# from .ThreelayermitosisSteppables import ECMRemodelingSteppable
# CompuCellSetup.register_steppable(steppable=ECMRemodelingSteppable(frequency=1))   

from ThreelayermitosisSteppables import MitosisSteppable

CompuCellSetup.register_steppable(steppable=MitosisSteppable(frequency=1))
# from ThreelayermitosisSteppables import FieldInitializerSteppable
# CompuCellSetup.register_steppable(steppable=FieldInitializerSteppable(frequency=1))

CompuCellSetup.run()





