from cc3d.core.PySteppables import *
import numpy as np
from random import randint

class ThreelayermitosisSteppable(SteppableBasePy):

    def __init__(self, frequency=1):
        SteppableBasePy.__init__(self, frequency)
        self.cell_type_parameters = {}
        self.water_fraction = 0.1
        self.medium_cell = None
        self.s1 = 1
        
    def add_cell_type_parameters(self, cell_type, count, target_volume, lambda_volume):
        self.cell_type_parameters[cell_type] = [count, target_volume, lambda_volume]

    def set_fraction_of_water(self, water_fraction):
        if 0.0 < water_fraction < 1.0:
            self.water_fraction = water_fraction    

    def start(self):

        # Define targetVolume and lambdaVolume for both cell types
        self.add_cell_type_parameters(cell_type=1, count=0, target_volume=25.0, lambda_volume=10.0)  # real cells
        self.add_cell_type_parameters(cell_type=5, count=0, target_volume=10.0, lambda_volume=2.0)   # ECM cells

        # number_of_pixels = self.dim.x * self.dim.y
        number_of_pixels = 400 * 50

        count_type1 = int(number_of_pixels * (1 - self.water_fraction) / self.cell_type_parameters[1][1])
        count_type5 = int(number_of_pixels * self.water_fraction / self.cell_type_parameters[5][1])

        self.cell_type_parameters[1][0] = count_type1
        self.cell_type_parameters[5][0] = count_type5

        self.medium_cell = self.cellField[0, 0, 0]

        for cell_type, cell_type_param_list in self.cell_type_parameters.items():
            # initialize self.cellTypeParameters[0]+1 number of randomly
            # placed cells with user specified targetVolume and lambdaVolume
            for cell_count in range(cell_type_param_list[0]):
                cell = self.potts.createCell()
                self.cell_field[
                    randint(0, 400), randint(0, 150), randint(0, self.dim.z - 1)] = cell

                cell.type = 1
                cell.targetVolume = cell_type_param_list[1]
                cell.lambdaVolume = cell_type_param_list[2]

                # coord = (x, y, z)
                # if coord not in occupied:
                    # cell = self.potts.createCell()
                    # self.cell_field[x, y, z] = cell

                    # cell.type = cell_type
                    # cell.targetVolume = target_vol
                    # cell.lambdaVolume = lambda_vol

                    # occupied.add(coord)
                    # placed += 1
                # attempts += 1
                
                
    # def step(self, mcs):

        # if mcs == 500:
            # self.adjust_gravity()

        # if mcs == 300:
            # for cell in self.cellList:
                # if cell.type == 1:
                    # cell.lambdaVolume = 0.0
                # if cell.type == 2:
                    # cell.lambdaVolume = 10.0

       
        # if mcs == 200:
            # for x, y, z in ((x, y, z) for x, y, z in self.every_pixel() if 0 <= x <= 400 and 0 <= y <= 150):
                # current_cell = self.cell_field[x, y, z]
                
                
                # if not current_cell:
                    # cell = self.potts.createCell()
                    # self.cellField[x, y, z] = cell
                    # cell.type = 5
                    # cell.targetVolume = self.cell_type_parameters[5][1]
                    # cell.lambdaVolume = self.cell_type_parameters[5][2]
  

# class ECMRemodelingSteppable(SteppableBasePy):
    # def __init__(self, frequency=1):
        
        # SteppableBasePy.__init__(self, frequency)
        # self.s1 = 1
    
    
    # def step(self, mcs):
        # for cell in self.cell_list_by_type(self.s1):
            # for pixel in self.get_cell_pixel_list(cell):
                # x = pixel.pixel.x
                # y = pixel.pixel.y
                # z = pixel.pixel.z
                
                
                # if 0 <= x <= 500 and 0 <= y <= 100:
                    # self.field.matrix[x, y, z] += 0.05  # Adjust secretion rate as needed
           
          
         
        
class MitosisSteppable(MitosisSteppableBase):
    
    def __init__(self, frequency=1):
        MitosisSteppableBase.__init__(self, frequency)
        
        self.s1 = 1
        self.s2 = 4

    # def start(self):
        # field = self.field.MATRIX
        # for x in range(0, 400):
            # for y in range(0, 150):
                # for z in range(0, self.dim.z):  # if 3D
                    # field[x, y, z] = 1.0  # Set desired uniform value    
                    
                    # if not (0 <= x < 400 and 0 <= y < 150):
                        # field[x, y, z] = 0.0  # Reset outside region to 0
                        
    def step(self, mcs):
        field = self.field.MATRIX
        for x in range(self.dim.x):
            for y in range(151, self.dim.y):  # y > 150
                for z in range(self.dim.z):
                    field[x, y, z] = 0.0  # Clear out unwanted diffusion               
      
        if mcs > 0 and mcs % 50 == 0:
            
            for cell in self.cell_list_by_type(self.s1):
                    if (0 < cell.xCOM < 400 and 120 < cell.yCOM < 150):
                    # print(f"Dividing cell ID {cell.id} at position x={cell.xCOM}")
                        if cell.volume == 25:  # example condition
                            self.divide_cell_random_orientation(cell)

                            

                            
    def update_attributes(self):
        # Mandatory for MitosisSteppableBase
        self.clone_parent_2_child()  # copies parent attributes to daughters

        if self.parent_cell.type == self.s1:
            self.child_cell.type = self.s1
        
    
                            
        
 
 