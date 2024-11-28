
from cc3d import CompuCellSetup
        

from NewSimulationSteppables import ConcentricTubeSteppable

CompuCellSetup.register_steppable(steppable=ConcentricTubeSteppable(frequency=1))


CompuCellSetup.run()
