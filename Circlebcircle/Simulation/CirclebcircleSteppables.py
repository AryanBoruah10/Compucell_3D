from cc3d.core.PySteppables import *

class CirclebcircleSteppable(SteppableBasePy):

    def __init__(self,frequency=1):

        SteppableBasePy.__init__(self,frequency)

    def start(self):
        """
        any code in the start function runs before MCS=0
        """
        cell = self.new_cell(self.A)
        cell.targetVolume = 8000
        cell.lambdaVolume = 10.0
        self.cell_field[int(self.dim.x/2), int(self.dim.y/2), 0] = cell
        
        cell = self.new_cell(self.B)
        cell.targetVolume = 1000
        cell.lambdaVolume = 30.0
        self.cell_field[int(self.dim.x/3), int(self.dim.y/3), 0] = cell
        


    def step(self,mcs):
        """
        type here the code that will run every frequency MCS
        :param mcs: current Monte Carlo step
        """

        # for cell in self.cell_list:
        #
        #     print("cell.id=",cell.id)

    def finish(self):
        """
        Finish Function is called after the last MCS
        """