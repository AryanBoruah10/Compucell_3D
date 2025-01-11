from cc3d.core.PySteppables import *
import numpy as np

class CPM_circularSteppable(SteppableBasePy):

    def __init__(self, frequency=1):

        SteppableBasePy.__init__(self, frequency)
        


    def start(self):
        center_x = int(self.dim.x / 2)  # Calculate center X
        center_y = int(self.dim.y / 2)  # Calculate center Y
        cell = self.new_cell(self.SC)  # Create an SC cell
        self.cell_field[center_x, center_y, 0] = cell
        """
        Called before MCS=0 while building the initial simulation
        """

    def step(self, mcs):
        """
        Called every frequency MCS while executing the simulation
        
        :param mcs: current Monte Carlo step
        """

        for cell in self.cell_list:

            print("cell.id=",cell.id)

    def finish(self):
        """
        Called after the last MCS to wrap up the simulation
        """

    def on_stop(self):
        """
        Called if the simulation is stopped before the last MCS
        """
