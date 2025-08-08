from cc3d.core.PySteppables import *
import numpy as np



class ConstraintInitializerSteppable(SteppableBasePy):
    def __init__(self,frequency=1):
        SteppableBasePy.__init__(self,frequency)

    def start(self):

        # for cell in self.cell_list:

            # cell.targetVolume = 25
            # cell.lambdaVolume = 2.0
            
            
            
        for cell in self.cell_list_by_type(self.STRM_1):  # setup the stromal cells
           cell.targetVolume = 100 # Stroma is large 
           cell.lambdaVolume = 25
        
        for cell in self.cell_list_by_type(self.MATRIX):  # setup the matrix cells
           cell.targetVolume = 25  # matrix is small 
           cell.lambdaVolume = 12  
    


    
        
# class GrowthSteppable(SteppableBasePy):
    # def __init__(self,frequency=1):
        # SteppableBasePy.__init__(self, frequency)

    # def step(self, mcs):
    
        # for cell in self.cell_list:
            # cell.targetVolume += 1        

        # # alternatively if you want to make growth a function of chemical concentration uncomment lines below and comment lines above        

        # field = self.field.CHEMICAL_FIELD_NAME
        
        # for cell in self.cell_list:
            # concentrationAtCOM = field[int(cell.xCOM), int(cell.yCOM), int(cell.zCOM)]

            # # you can use here any fcn of concentrationAtCOM
            # cell.targetVolume += 0.01 * concentrationAtCOM       

        
class MitosisSteppable(MitosisSteppableBase):
    def __init__(self,frequency=1):
        MitosisSteppableBase.__init__(self,frequency)

    def step(self, mcs):
        
        if mcs % 50 == 0:
            cells_to_divide=[]
            for cell in self.cell_list:
                if cell.type == self.STRM_1 and cell.volume > 150:
                    cells_to_divide.append(cell)
                    
                    
                if cell.type == self.MATRIX and cell.volume>45:  # matrix is small
                    cells_to_divide.append(cell)    
            
            
            for cell in cells_to_divide:
                self.divide_cell_along_minor_axis(cell)


    def update_attributes(self):
        # reducing parent target volume
        self.parent_cell.targetVolume /= 2.0                  

        self.clone_parent_2_child()            

        # for more control of what gets copied from parent to child use cloneAttributes function
        # self.clone_attributes(source_cell=self.parent_cell, target_cell=self.child_cell, no_clone_key_dict_list=[attrib1, attrib2]) 
        
        # if self.parent_cell.type==1:
            # self.child_cell.type=2
        # else:
            # self.child_cell.type=1

        