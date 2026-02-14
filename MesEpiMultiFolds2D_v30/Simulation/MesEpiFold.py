
from cc3d import CompuCellSetup
        

from MesEpiFoldSteppables import CellGradualAddition

CompuCellSetup.register_steppable(steppable=CellGradualAddition(frequency=1))



        
from MesEpiFoldSteppables import FetchCoordsandApplyForces
CompuCellSetup.register_steppable(steppable=FetchCoordsandApplyForces(frequency=1))



from MesEpiFoldSteppables import MuscleCellMitosis
CompuCellSetup.register_steppable(steppable=MuscleCellMitosis(frequency=1))

CompuCellSetup.run()
