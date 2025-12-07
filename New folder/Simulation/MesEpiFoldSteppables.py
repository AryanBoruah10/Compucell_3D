from cc3d.core.PySteppables import *
import numpy as np
import os 
import logging
import math

class MesEpiFoldSteppable(SteppableBasePy):

    def __init__(self, frequency=1):

        SteppableBasePy.__init__(self,frequency)

    def start(self):
        """
        Called before MCS=0 while building the initial simulation
        """
        # Make sure ExternalPotential plugin is loaded
        cell1 = self.cell_field[125, 230, 0]
        cell2 = self.cell_field[175, 230, 0]
        # cell3 = self.cell_field[225, 130, 0]
        # cell4 = self.cell_field[475, 130, 0]
        cell5 = self.cell_field[525, 230, 0]
        cell6 = self.cell_field[575, 230, 0]
        self.shared_steppable_vars['moving_muscle_cell_lambdaVecY'] = 3.0 #define a global variable for force component pointing along Y axi
        # fetch the variable
        cell1.lambdaVecY = self.shared_steppable_vars['moving_muscle_cell_lambdaVecY'] 
        cell2.lambdaVecY = self.shared_steppable_vars['moving_muscle_cell_lambdaVecY']  
        # cell3.lambdaVecY = self.shared_steppable_vars['moving_muscle_cell_lambdaVecY']
        # cell4.lambdaVecY = self.shared_steppable_vars['moving_muscle_cell_lambdaVecY']
        cell5.lambdaVecY = self.shared_steppable_vars['moving_muscle_cell_lambdaVecY'] 
        cell6.lambdaVecY = self.shared_steppable_vars['moving_muscle_cell_lambdaVecY']
        #setting the global variable
        self.shared_steppable_vars['moving_muscle_cell1'] = cell1
        self.shared_steppable_vars['moving_muscle_cell2'] = cell2
        # self.shared_steppable_vars['moving_muscle_cell3'] = cell3
        # self.shared_steppable_vars['moving_muscle_cell4'] = cell4
        self.shared_steppable_vars['moving_muscle_cell5'] = cell5
        self.shared_steppable_vars['moving_muscle_cell6'] = cell6
        #adding external force towards the middle for cells EPI and ECM
        # iterating over cells of type 1
            # list of  cell types (capitalized)
            
        
        
        
        
           
            
            
            
        
        
        
        #create fpp links for epithelial cells
        # iterating over cells of type 1
        # list of  cell types (capitalized)
        # for cell in self.cell_list_by_type(self.EPI):
            # # you can access/manipulate cell properties here
            # # print ("id=", cell.id, " type=", cell.type)
            # for neighbor, common_surface_area in self.get_cell_neighbor_data_list(cell):
                # if neighbor:
                    # if neighbor.type==self.EPI:
                         # link = self.new_fpp_link(cell, neighbor, 10, 7, 1000)

            
        
        # Make sure FocalPointPlacticity plugin is loaded
        # Arguments are:
        # initiator: CellG, initiated: CellG, lambda_distance: float, target_distance: float, max_distance: float
       
        
        
        
        
    def step(self, mcs):

        if mcs % 6000==0 and mcs>=10:
                x = 0
                y = 278
                size = 7
                cell = self.new_cell(self.EPI)
                # size of cell will be SIZExSIZEx1
                self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell

                # for neighbor, common_surface_area in self.get_cell_neighbor_data_list(cell):
                    # if neighbor:
                        # if neighbor.type==self.EPI:
                             # link = self.new_fpp_link(cell, neighbor, 10, 7, 1000)
                
                x = 0
                y = 271
                size = 7
                cell = self.new_cell(self.ECM)
                # size of cell will be SIZExSIZEx1
                self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell
           
            
        
        if mcs % 6000==0:
                x = 0
                y = 250
                size = 7
                cell = self.new_cell(self.STROMA)
                # size of cell will be SIZExSIZEx1
                self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell
                
                x = 0
                y = 257
                size = 7
                cell = self.new_cell(self.STROMA)
                # size of cell will be SIZExSIZEx1
                self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell
                
                x = 0
                y = 264
                size = 7
                cell = self.new_cell(self.STROMA)
                # size of cell will be SIZExSIZEx1
                self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell    
        
        if mcs % 4800==0 and mcs>=10:
            x = 0
            y = 200
            size = 7
            cell = self.new_cell(self.MUSCLE)
            # size of cell will be SIZExSIZEx1
            self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell

            # for neighbor, common_surface_area in self.get_cell_neighbor_data_list(cell):
                # if neighbor:
                    # if neighbor.type==self.EPI:
                         # link = self.new_fpp_link(cell, neighbor, 10, 7, 1000)  
        
        # if mcs%100==0 and mcs<4000:
            # for cell in self.cell_list_by_type(self.EPI, self.ECM):
                # # you can access/manipulate cell properties here
                # # if cell.xCOM<self.dim.x:
                    # # direction = -1
                # # else:
                    # # direction = +1
                    # direction = (cell.xCOM-(self.dim.x/2))/(self.dim.x/2)
                    # if cell.xCOM<175 or cell.xCOM>525:    
                            # cell.lambdaVecX = direction*0.5  # force component pointing along X axis - towards positive X's
                # # Make sure ExternalPotential plugin is loaded
                    # else: 
                            # cell.lambdaVecX = direction*-0.5 
                
                
        # if mcs>=4000 and mcs%100==0:
                # for cell in self.cell_list_by_type(self.EPI, self.ECM):
                # # you can access/manipulate cell properties here
                # # if cell.xCOM<self.dim.x:
                    # # direction = -1
                # # else:
                    # # direction = +1
                        # direction = (cell.xCOM-(self.dim.x/2))/(self.dim.x/2)
                
                # #assign force direction based on location of cell
                        # if cell.xCOM<175 or cell.xCOM>525:
                                # cell.lambdaVecX = direction*1.0  # force component pointing along X axis - towards positive X's  
                        # else:
                                # cell.lambdaVecX = direction*-1.0    
                
        # if mcs>=4000 and mcs%100==0:
            # for cell in self.cell_list_by_type(self.STROMA):
                # # you can access/manipulate cell properties here
                # # if cell.xCOM<self.dim.x:
                    # # direction = -1
                # # else:
                    # # direction = +1
                # direction = (cell.xCOM-(self.dim.x/2))/(self.dim.x/2)    
                # if cell.xCOM<175 or cell.xCOM>525:
                    # cell.lambdaVecX = direction*0.5  # force component pointing along X axis - towards positive X's       
                # else:
                    # cell.lambdaVecX = direction*-0.5  
            
            # for cell in self.cell_list_by_type(self.STROMA):
                # # you can access/manipulate cell properties here
                # # if cell.xCOM<self.dim.x:
                    # # direction = -1
                # # else:
                    # # direction = +1
                # # direction = (cell.xCOM-(self.dim.x/2))/(self.dim.x/2)    
                # if 125<cell.xCOM<225 or 500<cell.xCOM<600:
                    # cell.lambdaVecY = direction*2.5  # force component pointing along Y axis - towards positive X's
             
        # if mcs>=4000 and mcs%100==0:
                # for cell in self.cell_list_by_type(self.MUSCLE):
                # # you can access/manipulate cell properties here
                # # if cell.xCOM<self.dim.x:
                    # # direction = -1
                # # else:
                    # # direction = +1
                  
            
                        # if 125<cell.xCOM<225 or 500<cell.xCOM<600:
                                # cell.lambdaVecY = 8.0 #force in the Y direction for central stromal cells
                    
        
        
   
        
class FetchCoordsSteppable(SteppableBasePy):
    def __init__(self, frequency=1):
        
        SteppableBasePy.__init__(self, frequency)
        # PLACE YOUR CODE BELOW THIS LINE
        
        
        
        ## This code should geeralize to varied muscle cell size also. 
        
        self.start_fold_coord = 174 ## We can play with the variables 
        self.fold_seperation = 350 ## Ideal seperation is 350 ##    ## we can play with this variable 
        
        
    def arithProg(self, n):
        
            list_range = list(range(1, int(self.dim.x)))
            list_nums = []

            for x in list_range:

                    if x%n == 0:
                            list_nums.append(x)

                    total_nums = len(list_nums)      

            return list_nums


    def muscle_coordinates(self):
        
        
                muscle_coords = []
                muscle_new_coords = []
                muscle_cell_com = []
                muscle_x_coords = []
        
                for cell in self.cell_list_by_type(self.MUSCLE):
                        # print("The structure of cell.xCOM is: ", str(cell.xCOM))  if we remove int(cell.xCOM) the str of cell.xCOM will be 174.49999999 
                        x = int(cell.xCOM)
                        y = int(cell.yCOM)
                        z = int(cell.zCOM)
            
                        muscle_coords.append((x, y, z, cell.id, cell.type))
            
        # print("Muscle cell COM coordinates:", muscle_coords) 
        
        
                len_muscle = len(muscle_coords)
                # print("The structure of self.dim.x is: ", str(self.dim.x))
                
                
                for cell in self.cell_list_by_type(self.MUSCLE):
                        x = int(cell.xCOM)
                        muscle_cell_com.append(x)
        
        
                num_fold = (self.dim.x - self.start_fold_coord)//self.fold_seperation
                num_fold = num_fold + 1
                
        
        
                if self.fold_seperation * num_fold <= self.dim.x:
                    
                        for cell in self.cell_list_by_type(self.MUSCLE):
                            
                                if int(cell.xCOM) >= self.start_fold_coord:
                                        for nums in muscle_cell_com:
                                                if nums >= self.start_fold_coord:
                                                        muscle_new_coords.append(((self.start_fold_coord), int(cell.yCOM), 0, cell.type))
                                                        muscle_x_coords.append(self.start_fold_coord)
                                                        self.start_fold_coord = self.start_fold_coord + self.fold_seperation
                                                        
                                                        
                                                        if self.start_fold_coord >  self.dim.x:
                                                            
                                                                break
                                                                
                                                                
                                                       
                else:
                        print("THE SEPERATION IS OUT OF BOUND")
                                                                
                                                             
                        # for cell in self.cell_list_by_type(self.MUSCLE):
                                # x_com = int(cell.xCOM)
                                # y_com = int(cell.yCOM)

                                # # If the cell is exactly at the starting fold coordinate
                                # if x_com >= self.start_fold_coord:
                                        # for nums in muscle_cell_com:
                                                # if nums > self.start_fold_coord:
                                                        # muscle_new_coords.append((self.start_fold_coord, y_com, 0, cell.type))

                                                # # Update the fold coordinate
                                                        # self.start_fold_coord += self.fold_seperation

                                                # # Check against the boundary every time after updating
                                                        # if int(self.start_fold_coord) > int(1000):
                                                                # break                               
                                                                                
                                                            
                                                        
                                                
                                                


                # muscle_new_coords.append((x , y, z, cell.type))
                muscle_to_fold = [] 
                
                
                for temp in muscle_x_coords: 
                    muscle_to_fold.append(temp) 
                    result = temp + 50 
                    muscle_to_fold.append(result) 
                # print("these are the nums",muscle_to_fold) 
                # print("these are wuevwecvfweycv", muscle_coords) return muscle_to_fold
                
                
                print(muscle_to_fold)
        
                return muscle_to_fold
                
       
                
        
        
        
    def fetch_main_coordinates(self, no_fold, spread):              ## For now this fucntion is doing nothing ##
        
        
        coordinates = []
        specific_coords = []
        
        
        all_coords = self.arithProg(n = int(int(self.dim.x)/no_fold))
        
        for center in all_coords:
                for x in range(center - spread, center + spread + 1):
                        if 0 <= x < int(self.dim.x):
                                specific_coords.append(x)
                              
        
        
        for x in specific_coords:
                for y in range(int(self.dim.y)):
                        for z in range(int(self.dim.z)):
                                cell = self.cell_field[x,y,z]
                                if cell:
                                        coordinates.append((x, y, z, cell.id, cell.type))
                    
                    
        # print("these are the specifics", coordinates)           
                    
        return coordinates  
        
        
        
        

    def start(self):
        
        
        '''
        for cell in self.cell_list:
                if cell.type == self.STROMA:
                # field 'F' must match the XML chemical field name
                    cd = self.chemotaxisPlugin.addChemotaxisData(cell, "ECgrad")
                    cd.setLambda(20.0)
                    cd.assignChemotactTowardsVectorTypes([self.EPI, self.MEDIUM, self.MUSCLE, self.ECM])
                    
        '''
        try:
                # global_coords = self.fetch_main_coordinates(no_fold = 3, spread = 50)
                self.muscle_fold_coordinates = self.muscle_coordinates()
            
            
                print("POINTS AT WHICH MUSCLE WILL FOLD: ", self.muscle_fold_coordinates)
                print("THE NUMBER OF FOLDS WE GET: ", len(muscle_fold_coordinates))
                # print("GLOBAL COORDS: ", global_coords)
            
                # print("LENGTH OF THE GLOBAL MUSCLE COORDS: ", len(muscle_fold_coordinates))
                # print("GLOBAL COORDS: ", len(global_coords))
            
            
                output_path_1 = os.path.join(self.output_dir, "muscle_fold_coordinates.txt")
                output_path_2 = os.path.join(self.output_dir, "all_muscle_cell_coordinates.txt")
            
            

            # Open file for writing
                with open(output_path_1, "w") as f:
                        f.write("x,y,z,cell_id,cell_type\n")  # Header
                        
                        
                        ## ignore this code for now just let it run##
                        coords = self.fetch_main_coordinates(no_fold = 3, spread = 50) ## {n} is no of folds and {m} is the spread of the cells that I want to fold ##
                                # Save only occupied lattice points
                        for (x, y, z, cell_id, cell_type) in coords:
                                f.write(f"{x},{y},{z},{cell_id},{cell_type}\n")
                    
                    
                    
                    
                with open(output_path_2, "w") as f:
                        f.write("x,y,z,cell_id,cell_type\n")
                       
                        muscle_coords = self.muscle_coordinates() 
                        for (x, y, z, cell_id, cell_type) in muscle_coords:
                                f.write(f"{x},{y},{z},{cell_id},{cell_type}\n")
                    
                
                
                # if cell:
                    # f.write(f"{x},{y},{z},{cell.id},{cell.type}\n")

                # print(f"Coordinates saved to: {output_path_1}")
                # print(f"Muscle Coordinates saved to: {output_path_2}")
        
        except Exception as e:
                logging.error(f"startfileError occurred: {str(e)}")
            
        
           

    def step(self, mcs):
        
        temp = self.muscle_fold_coordinates
        
        
        self.stromaCell_force = 10.0        #user input      2.5 -------> 5.0
        self.stromaDecay = 0.001
        self.muscleCell_force = 20.0             #user input 8 ----> 15 -----> 20
        self.muscleDecay = 0.0001
        
        
        if mcs >= 5500 and mcs % 100:   # <-- Start chemotaxis here
        
        
            for cell in self.cell_list:
                if cell.type == self.STROMA:
                # field 'F' must match the XML chemical field name
                    cd = self.chemotaxisPlugin.addChemotaxisData(cell, "ECgrad")
                    cd.setLambda(10.0)
                    cd.assignChemotactTowardsVectorTypes([self.EPI, self.MEDIUM, self.MUSCLE, self.ECM])
                    

            print("Turning ON chemotaxis at MCS =", mcs)
    
            # Applying lambda to all cells of a given type
            for cell in self.cell_list:
                if cell.type == self.STROMA:
                    if int(cell.xCOM) in self.muscle_fold_coordinates:               ## Here we are specifying the coords of stromal cells to fold
                        print("the values are:", int(cell.xCOM))
                
                        cd = self.chemotaxisPlugin.getChemotaxisData(cell, "ECgrad")
                        if cd:
                            lm = cd.getLambda()
                            cd.setLambda(lm)
                        
                
        
        
        
        if mcs%100==0 and mcs<4000:
            
            
            for cell in self.cell_list_by_type(self.EPI, self.ECM):
                # you can access/manipulate cell properties here
                # if cell.xCOM<self.dim.x:
                    # direction = -1
                # else:
                    # direction = +1
                    direction = (cell.xCOM-(self.dim.x/2))/(self.dim.x/2)
                    if cell.xCOM < temp[0] or cell.xCOM > temp[-1]:    
                            cell.lambdaVecX = direction*0.5  # force component pointing along X axis - towards positive X's
                # Make sure ExternalPotential plugin is loaded
                    else: 
                            cell.lambdaVecX = direction*-0.5 
                
                
        if mcs>=4000 and mcs%100==0:
                for cell in self.cell_list_by_type(self.EPI, self.ECM):
                # you can access/manipulate cell properties here
                # if cell.xCOM<self.dim.x:
                    # direction = -1
                # else:
                    # direction = +1
                        direction = (cell.xCOM-(self.dim.x/2))/(self.dim.x/2)
                
                #assign force direction based on location of cell
                        if cell.xCOM < temp[0] or cell.xCOM > temp[-1]:
                                cell.lambdaVecX = direction*1.0  # force component pointing along X axis - towards positive X's  
                        else:
                                cell.lambdaVecX = direction*-1.0    
        
        
        
        # print("STEP called at MCS:", mcs)
        # print("this is temp", temp)
        

        # if mcs >= 50 and mcs % 50 == 0:
            # temp = self.muscle_fold_coordinates
            # print("this is temp", temp)
            
            
            
            
        if mcs>=4000 and mcs%100==0:
                A = temp   # Example: fold coordinate list

              # Apply X-direction forces (same as before)
                for cell in self.cell_list_by_type(self.STROMA):
                    direction = (cell.xCOM - (self.dim.x / 2)) / (self.dim.x / 2)

                    if cell.xCOM < A[0] or cell.xCOM > A[-1]:
                        cell.lambdaVecX = direction * 0.5
                    else:
                        cell.lambdaVecX = direction * -0.5

                # Apply Y-direction forces based on ranges in A
                
                # for cell in self.cell_list_by_type(self.STROMA):
                    # # direction = (cell.xCOM - (self.dim.x / 2)) / (self.dim.x / 2)

                    # # iterate through consecutive coordinate pairs
                    # for i in range(0, len(A), 2):
                        # lower = A[i]
                        # upper = A[i + 1]

                        # if lower < cell.xCOM < upper:
                            # cell.lambdaVecY = self.stromaCell_force
                            # break   # break once matched (avoids reassigning multiple times)

            
                F0 = self.stromaCell_force                  # base (peak) lambdaVecY at a fold center
                decay_rate = self.stromaDecay                           # exponential decay rate (larger -> faster decay)
                fold_centers = self.muscle_fold_coordinates  # x positions of the two fold centers (example)
                apply_halfwidth = 120                        # optional: only apply force if abs(dx) < apply_halfwidth
                max_lambda = 200.0                           # safety clamp for lambdaVecY

                
                """
                Apply Y-directed forces that are strongest at each x in fold_centers and
                decay away exponentially. Cells above center_y are pulled downward;
                cells below are pulled upward (so tissue bends inward).
                """

                center_y = self.dim.y / 2.0                                # Center of Y axis 

                # Precompute: keep fold centers as floats
                centers = [float(c) for c in fold_centers]                 # converting every fold center coordinate to float for consistency.

                # Iterate over whichever cell list you want (STROMA, MUSCLE, epithelium...). 
                # Use self.cell_list_by_type(self.STROMA) if you want only stromal cells.
                for cell in self.cell_list_by_type(self.MUSCLE):  
                    xcell = float(cell.xCOM)
                    ycell = float(cell.yCOM)

                    # compute combined contribution from both fold centers
                    Fy = 0.0
                    for cx in centers:                                        # Cells feel force from each fold simultaneously.
                        dx = abs(xcell - cx)                                  # Distance from fold center → controls exponential decay.
                        # optionally skip far away to save compute and avoid tiny forces
                        if dx <= apply_halfwidth:                             # If the cell is farther than ±120 pixels, skip force contribution.
                            Fy += F0 * math.exp(-decay_rate * dx)             # main decay equation 

                    # clamp / safety
                    if Fy > max_lambda:
                        Fy = max_lambda                # Safety: avoid overly large forces.

                    # if force is extremely tiny, zero it out (optional)
                    if Fy < 1e-6:
                        cell.lambdaVecY = 0.0
                        # optionally clear targetVecY too
                        # cell.targetVecY = 0.0
                        continue

                    # choose direction: cells above center_y should move down, below move up
                    # We set targetVecY to -1.0 (down) if ycell > center_y, else +1.0 (up).
                    # This ensures the sign/directon is correct; lambda is magnitude.
                    if ycell > center_y:
                        cell.targetVecY = -1.0
                    else:
                        cell.targetVecY = +1.0

                    # apply magnitude
                    cell.lambdaVecY = Fy

                    # Optionally set targetVecX to 0 to avoid accidental X bias
                    cell.targetVecX = 0.0
                
            
            
            
        if mcs>=4000 and mcs%100 == 0:
            F0 = self.muscleCell_force                   # base (peak) lambdaVecY at a fold center
            decay_rate = 0.02                            # exponential decay rate (larger -> faster decay)
            fold_centers = self.muscle_fold_coordinates  # x positions of the two fold centers (example)
            apply_halfwidth = 120                        # optional: only apply force if abs(dx) < apply_halfwidth
            max_lambda = 200.0                           # safety clamp for lambdaVecY

            
            """
            Apply Y-directed forces that are strongest at each x in fold_centers and
            decay away exponentially. Cells above center_y are pulled downward;
            cells below are pulled upward (so tissue bends inward).
            """

            center_y = self.dim.y / 2.0

            # Precompute: keep fold centers as floats
            centers = [float(c) for c in fold_centers]

            # Iterate over whichever cell list you want (STROMA, MUSCLE, epithelium...). 
            # Use self.cell_list_by_type(self.STROMA) if you want only stromal cells.
            for cell in self.cell_list_by_type(self.MUSCLE):  
                xcell = float(cell.xCOM)
                ycell = float(cell.yCOM)

                # compute combined contribution from both fold centers
                Fy = 0.0
                for cx in centers:
                    dx = abs(xcell - cx)
                    # optionally skip far away to save compute and avoid tiny forces
                    if dx <= apply_halfwidth:
                        Fy += F0 * math.exp(-decay_rate * dx)

                # clamp / safety
                if Fy > max_lambda:
                    Fy = max_lambda

                # if force is extremely tiny, zero it out (optional)
                if Fy < 1e-6:
                    cell.lambdaVecY = 0.0
                    # optionally clear targetVecY too
                    # cell.targetVecY = 0.0
                    continue

                # choose direction: cells above center_y should move down, below move up
                # We set targetVecY to -1.0 (down) if ycell > center_y, else +1.0 (up).
                # This ensures the sign/directon is correct; lambda is magnitude.
                if ycell > center_y:
                    cell.targetVecY = -1.0
                else:
                    cell.targetVecY = +1.0

                # apply magnitude
                cell.lambdaVecY = Fy

                # Optionally set targetVecX to 0 to avoid accidental X bias
                cell.targetVecX = 0.0
            
        
            
            
            
            
            
            
            
            
            
            
            
            
           
        
        
        pass
        
        
        
        
        
        
     
        
        
        
        
        
        

