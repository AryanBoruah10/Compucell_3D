from cc3d import CompuCellSetup
        

from CirclebcircleSteppables import CirclebcircleSteppable

CompuCellSetup.register_steppable(steppable=CirclebcircleSteppable(frequency=1))


CompuCellSetup.run()