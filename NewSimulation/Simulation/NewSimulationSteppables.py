from cc3d.core.PySteppables import *
import numpy as np


class ConcentricTubeSteppable(SteppableBasePy):
    def __init__(self, frequency=1):
        SteppableBasePy.__init__(self, frequency)

    def start(self):
        """
        Initializes the simulation by creating concentric tube structure with cells between the tubes.
        """
        # Get simulation dimensions
        x_size = self.dim.x
        y_size = self.dim.y
        z_size = self.dim.z

        # Define tube radii
        inner_radius = 10
        outer_radius = 30

        center_x = x_size // 2
        center_y = y_size // 2

        # Create cells between inner and outer tubes
        for x in range(x_size):
            for y in range(y_size):
                distance = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
                if inner_radius < distance <= outer_radius:
                    cell = self.new_cell(self.CELL)  # Define CELL type in XML
                    self.cell_field[x, y, 0] = cell

    def step(self, mcs):
        """
        Called every MCS during the simulation.
        """
        for cell in self.cell_list:
            print(f"Cell ID: {cell.id}, Volume: {cell.volume}")

    def finish(self):
        """
        Wrap up the simulation after the last MCS.
        """
        print("Simulation finished.")
