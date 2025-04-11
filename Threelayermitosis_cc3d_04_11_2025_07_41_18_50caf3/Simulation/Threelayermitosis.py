
from cc3d import CompuCellSetup
        

from ThreelayermitosisSteppables import ThreelayermitosisSteppable

CompuCellSetup.register_steppable(steppable=ThreelayermitosisSteppable(frequency=1))


CompuCellSetup.run()
