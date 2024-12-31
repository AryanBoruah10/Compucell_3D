
from cc3d import CompuCellSetup
        

from CPM_circularSteppables import CPM_circularSteppable

CompuCellSetup.register_steppable(steppable=CPM_circularSteppable(frequency=1))


CompuCellSetup.run()
