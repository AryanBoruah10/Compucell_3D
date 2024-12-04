from cc3d.core.PySteppables import *
import numpy as np

class CircleSteppable(SteppableBasePy):

    def __init__(self, frequency=1):
        SteppableBasePy.__init__(self, frequency)

    def start(self):
        """
        Code in the start function runs before MCS=0. Here, we create concentric circles of cells.
        """
        # Define the radii for the inner and outer circle
        center_x = self.dim.x // 2
        center_y = self.dim.y // 2

        inner_radius = 10   # Radius for cell type B
        outer_radius = 20   # Radius for cell type A

        # Loop through the lattice points to create a concentric circle
        for x in range(self.dim.x):
            for y in range(self.dim.y):
                distance = np.sqrt((x - center_x) ** 2 + (y - center_y) ** 2)  # Distance from the center
                if distance <= inner_radius:  # Cells within the inner radius will be cell type B
                    cell = self.new_cell(self.B)
                    cell.targetVolume = 3000
                    cell.lambdaVolume = 10.0
                    self.cell_field[x, y, 0] = cell
                elif distance <= outer_radius:  # Cells between the inner and outer radius will be cell type A
                    cell = self.new_cell(self.A)
                    cell.targetVolume = 3000
                    cell.lambdaVolume = 10.0
                    self.cell_field[x, y, 0] = cell

    def step(self, mcs):
        """
        This function runs every frequency MCS (Monte Carlo Step).
        You can update the state of cells here.
        """
    def finish(self):
        """
        Finish Function is called after the last MCS. This can be used for cleanup.
        """
        print("Simulation finished.")