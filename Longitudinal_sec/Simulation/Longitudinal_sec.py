
from cc3d import CompuCellSetup
        

from Longitudinal_secSteppables import Longitudinal_secSteppable

CompuCellSetup.register_steppable(steppable=Longitudinal_secSteppable(frequency=1))


CompuCellSetup.run()
