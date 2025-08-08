from cc3d.core.PySteppables import *
import numpy as np



class ConstraintInitializerSteppable(SteppableBasePy):
    def __init__(self,frequency=1):
        SteppableBasePy.__init__(self,frequency)
        
        self.e1 = 2
        self.e2 = 3
        self.s1 = 1

    def start(self):

        for cell in self.cell_list:

            cell.targetVolume = 50 # 25
            cell.lambdaVolume = 2.0 # 2.0
            
            
        for cell in self.cell_list_by_type(self.e1):
            
            for cell2 in self.cell_list_by_type(self.e2):
                
                if cell.xCOM == cell2.xCOM:
                    self.reassign_cluster_id(cell, cell.clusterId)
                    break
                    
        
        
        for cell in self.cell_list_by_type(self.e2):
            for neighbor, common_surface_area in self.get_cell_neighbor_data_list(cell):
                if neighbor:
                    if(neighbor.type == self.e2):
                        # Make sure FocalPointPlacticity plugin is loaded
                        # Arguments are:
                        # initiator: CellG, initiated: CellG, lambda_distance: float, target_distance: float, max_distance: float
                        #link = self.new_fpp_link(initiator, initiated, lambda_distance, target_distance, max_distance)
                        link = self.new_fpp_link(cell, neighbor, 5, 7, 100) # 10, 7, 200
        
        
# class GrowthSteppable(SteppableBasePy):
    # def __init__(self,frequency=1):
        # SteppableBasePy.__init__(self, frequency)
        
        # self.e1 = 2
        # self.e2 = 3
        # self.s1 = 1
        # self.s2 = 4

    # def step(self, mcs):
        # for cell in self.cell_list:
            # cell.targetVolume += 1  
      

        # # alternatively if you want to make growth a function of chemical concentration uncomment lines below and comment lines above        

        # field = self.field.CHEMICAL_FIELD_NAME
        
        # for cell in self.cell_list:
            # concentrationAtCOM = field[int(cell.xCOM), int(cell.yCOM), int(cell.zCOM)]

            # # you can use here any fcn of concentrationAtCOM
            # cell.targetVolume += 0.01 * concentrationAtCOM  
                
class DynamicContactEnergySteppable(SteppableBasePy):
    def __init__(self, frequency=1):
        SteppableBasePy.__init__(self, frequency)
        self.e1 = 2
        self.e2 = 3

    def step(self, mcs):
        if mcs == 200:
            self.contactEnergy(self.e1, self.e2, 100)  # Change contact energy to 40
            # print("Contact energy between e1 and e2 changed to 40 at MCS 200")  

        
class MitosisSteppable(MitosisSteppableBase):
    def __init__(self,frequency=1):
        MitosisSteppableBase.__init__(self,frequency)
        
        self.e1 = 2
        self.e2 = 3
        self.s1 = 1
        self.s2 = 4
        
    def adjust_gravity(self):

        force_elem = self.get_xml_element('force')
        force_elem.y = 20    

    def step(self, mcs):
        
        # if (mcs == 200):
            # for cell in self.cell_list_by_type(self.s1):
                # if (125<self.s1<225):
                    # cell.targetVolume += 2
        # if mcs == 200:
        if mcs > 0 and mcs % 50 == 0:    
            for cell in self.cell_list_by_type(self.s1):
                if ((200 < cell.xCOM < 225) or (50 < cell.xCOM < 75)) and cell.yCOM < 120:
                    # print(f"Dividing cell ID {cell.id} at position x={cell.xCOM}")
                    self.divide_cell_random_orientation(cell)
                    
                    
            
                    
                
        
        
        if (mcs == 200):
            for cell in self.cell_list_by_type(self.e1):
                if (200 < cell.xCOM < 225) or (50 < cell.xCOM < 75):
                    for link in self.get_fpp_links_by_cell(cell):
                        # ld = link.getLambdaDistance()
                        link.setLambdaDistance(100.0)
                        # td = link.getTargetDistance()
                        link.setTargetDistance(3.0)
                    
                    
                    
        if mcs == 200:
            self.adjust_gravity()           
                    
                

        # cells_to_divide=[]
        # for cell in self.cell_list:
            # if cell.volume>50:
                # cells_to_divide.append(cell)

        # for cell in cells_to_divide:

            # self.divide_cell_random_orientation(cell)
            # # Other valid options
            # self.divide_cell_orientation_vector_based(cell,1,1,0)
            # self.divide_cell_along_major_axis(cell)
            # self.divide_cell_along_minor_axis(cell)

    def update_attributes(self):
        
        # reducing parent target volume
        self.parent_cell.targetVolume /= 2.0                  

    # Clone attributes to child cell
        self.clone_parent_2_child()

    # Set child cell type
        if self.parent_cell.type == self.e1:
            self.child_cell.type = self.s2  # Keep it as a blue cell
            self.child_cell.targetVolume = self.parent_cell.targetVolume * 0.75  # Reduce volume

        # Create FPP links between newly created blue cell and neighboring green cells
        # for neighbor, common_surface_area in self.get_cell_neighbor_data_list(self.child_cell):
            # if neighbor and neighbor.type == self.e1:  # If the neighbor is a green cell
                # link = self.new_fpp_link(self.child_cell, neighbor, 20, 5, 50)  
                # # print(f"FPP link created between new blue cell {self.child_cell.id} and green cell {neighbor.id}")
                
                
                
                # neighbor.lambdaVecX = 0.0  No force in X direction
                # neighbor.lambdaVecY = -100.0  Strong downward force
                # neighbor.lambdaVecZ = 0.0  No force in Z direction

        else:
            self.child_cell.type = self.s2  # Other type for non-blue parent cells
    
    


    