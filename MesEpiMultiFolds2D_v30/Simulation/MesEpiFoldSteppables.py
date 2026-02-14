from cc3d.core.PySteppables import *
import numpy as np
import os 
import logging
import math
import random

###########################################################################################
## IN THIS CLASS, FUNCTION OF GRADUAL ADDITION OF CELLS IN EPI, ECM, STROMA AND MUSCLE.  ##
###########################################################################################


class CellGradualAddition(SteppableBasePy):

    def __init__(self, frequency=1):

        SteppableBasePy.__init__(self,frequency)

    def start(self):
        
        print("simulation starts")
       
        
        
        
        
    def step(self, mcs):

        if mcs % 6000==0 and mcs>=10:
                x = 0
                y = 278
                size = 7
                cell = self.new_cell(self.EPI)
                # size of cell will be SIZExSIZEx1
                self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell

                
                
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
        
        ## Muscle cell addition from the boundaries is {OFF}
        # if mcs % 4800==0 and mcs>=10:
            # x = 0
            # y = 200
            # size = 7
            # cell = self.new_cell(self.MUSCLE)
            # # size of cell will be SIZExSIZEx1
            # self.cell_field[x:x + size - 1, y:y + size - 1, 0] = cell

            
                    
        
############################################################################    
##In THIS CLASS, THE FOLLOWING FUNCTIONS ARE ASSIGNED: ##
                        
    ##  1. AUTOMATING FETCHING OF FOLD COORDINATES ##
    ##  2. APPLYING FORCES IN STROMA AND MUSCLE CELLS IN A EXPONENTIAL GRADIENT. ## 
    ##     FORCES DECAY FROM CENTER TO OUTWARD DIRECTION ## 
                            

###########################################################################

        
class FetchCoordsandApplyForces(SteppableBasePy):
    def __init__(self, frequency=1):
        
        SteppableBasePy.__init__(self, frequency)
       
        
        
        
        ## This code should geeralize to varied muscle cell size also. 
        
        self.start_fold_coord = 174 # WE CAN PLAY WITH THIS VARIABLE 
        self.fold_seperation = 350 # IDEAL SEPERATION IS 350 ##    ## WE CAN PLAY WITH THIS VARIABLE

        
        # self.vectorField = self.create_vector_field_cell_level_py("VELOCITY") 
        
        
    def arithProg(self, n):
        
            list_range = list(range(1, int(self.dim.x)))
            list_nums = []

            for x in list_range:

                    if x%n == 0:
                            list_nums.append(x)

                    total_nums = len(list_nums)      

            return list_nums



    #-------------------------------------------------------------------------------------------
    ## THIS IS THE MAIN FUNCTION THAT STORES THE LIST OF COORDINATES OF MUSCLE CELLS TO FOLD ##
    #-------------------------------------------------------------------------------------------
    def muscle_coordinates(self):
        
        
                muscle_coords =     []  # STORES ALL THE MUSCLE CELL CORRDINATES
                muscle_new_coords = []  # THIS LIST STORING ALL THE X AND Y COORDS + CELL TYPE
                muscle_cell_com =   []  # LIST STORING ONLY THE X COORDINATES OF ALL THE MUSCLE CELLS 
                muscle_x_coords =   []  # LIST STORES THE SUMMATION OF MUSCLE CELL COORDS + THE FOLD SEPERATION. ONLY THE FOLD COORDS ARE STORED.
        
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
                        muscle_cell_com.append(x)    # STORING THE X CORRDS OF MUSCLE CELLS # 
        
        
                num_fold = (self.dim.x - self.start_fold_coord)//self.fold_seperation
                num_fold = num_fold + 1
                
        
        
                if self.fold_seperation * num_fold <= self.dim.x:                   
                        for cell in self.cell_list_by_type(self.MUSCLE):                            
                                if int(cell.xCOM) >= self.start_fold_coord:
                                        for nums in muscle_cell_com:
                                                if nums >= self.start_fold_coord:
                                                        muscle_new_coords.append(((self.start_fold_coord), int(cell.yCOM), 0, cell.type))  # THIS LIST STORING ALL THE X AND Y COORDS + CELL TYPE
                                                        muscle_x_coords.append(self.start_fold_coord)         # THIS LIST ONLY STORING MUSCLE CELL X COORDINATES
                                                        self.start_fold_coord = self.start_fold_coord + self.fold_seperation        
                                                        
                                                        
                                                        if self.start_fold_coord >  self.dim.x:
                                                            
                                                            
                                                                break
                                                                
                                                                
                                                       
                else:
                        print("THE SEPERATION IS OUT OF BOUND")
                                                                
                                                             
                        
                muscle_to_fold = []    
                
                
                for temp in muscle_x_coords: 
                    muscle_to_fold.append(temp) 
                    result = temp + 50 
                    muscle_to_fold.append(result) 
                # print("these are the nums",muscle_to_fold) 
                # print("these are wuevwecvfweycv", muscle_coords) return muscle_to_fold
                
                
                print(muscle_to_fold)
        
                return muscle_to_fold
                
       
                
        
    #-------------------------------------------------------------------------------------------------
    ## THIS FUNCTION FETCHES THE MAIN MUSCLE COORDINATES BASED ON NO OF FOLD AND SPREAD OF THE FOLD ##    
    #-------------------------------------------------------------------------------------------------
            
    def fetch_main_coordinates(self, no_fold, spread):              # FOR NOW THIS FUCNTION IS DOING NOTHING #
        
        
        
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
        
        ## USING THIS CODE BLOCK FOR CHEMOTAXIS IN START FUNCTION DOESNOT WORK ##
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
                
            
            
                output_path_1 = os.path.join(self.output_dir, "muscle_fold_coordinates.txt")
                output_path_2 = os.path.join(self.output_dir, "all_muscle_cell_coordinates.txt")
            
            

            # OPEN FILE FOR WRITING
                with open(output_path_1, "w") as f:
                        f.write("x,y,z,cell_id,cell_type\n")  # HEADER
                        
                        
                        ## ignore this code for now just let it run##
                        coords = self.fetch_main_coordinates(no_fold = 3, spread = 50) ## {n} is no of folds and {m} is the spread of the cells that I want to fold ##
                                # SAVE ONLY OCCUPIED LATTICE POINTS
                        for (x, y, z, cell_id, cell_type) in coords:
                                f.write(f"{x},{y},{z},{cell_id},{cell_type}\n")
                    
                    
                    
                    
                with open(output_path_2, "w") as f:
                        f.write("x,y,z,cell_id,cell_type\n")
                       
                        muscle_coords = self.muscle_coordinates() 
                        for (x, y, z, cell_id, cell_type) in muscle_coords:
                                f.write(f"{x},{y},{z},{cell_id},{cell_type}\n")
                    
                
                
                
        
        except Exception as e:
                logging.error(f"startfileError occurred: {str(e)}")
            
        
           

    def step(self, mcs):

        ## CODE BLOCK TO PUT VECTORS ON THE STROMAL CELLS TO TRACK THE MOTION OF THE CELLS ##
        '''
        for cell in self.cell_list_by_type(self.STROMA):
                        
                        cell.dict["oldXcm"]=cell.xCOM       # dict entry for old cell x CM
                        cell.dict["oldYcm"]=cell.yCOM
        
        
        timeinterval = 10      # time interval between cell events (source/sink)
        if mcs%timeinterval == 0:
        
        
            fieldV = self.vectorField
            
            
            for cell in self.cell_list_by_type(self.STROMA):
                    
                    CVelX=cell.dict["oldXcm"]/timeinterval  # cell x compon Vel
                    CVelY=cell.dict["oldYcm"]/timeinterval  # cell y compon Vel

                    fieldV[cell] = [CVelX, CVelY, 0.]       # filling the field with values
                    
                   
                    cell.dict["oldXcm"]=cell.xCOM                           # storing actual cell x CM
                    cell.dict["oldYcm"]=cell.yCOM   
            
        '''
        
                    
        
        #LENGTH CONTRAINT PLUGIN IS NOT WORKING IN THE CASE OF MUSCLE CELL FOLDING. THE PLUGIN IS WORKING BUT NOT SUITABLE FOR THE MODEL 
        '''
        if mcs >= 100:
                print("length constraint is active")
                for cell in self.cell_list:  
                            if cell.type == self.MUSCLE:
                                    if 300 < cell.xCOM < 500:
                                            self.lengthConstraintPlugin.setLengthConstraintData(cell, 2, 40)
                    
        '''
        temp = self.muscle_fold_coordinates
        
        
        self.stromaCell_force = 2.5        #user input      2.5 -------> 5.0 --------> 15
        self.stromaDecay = 0.02
        self.muscleCell_force = 10.0        #user input      8 ----> 15 -----> 20 ----> 30
        self.muscleDecay = 0.02
        
        
        if mcs >= 5600 and mcs % 56:   # <-- START CHEMOTAXIS HERE
        
        
                for cell in self.cell_list:
                        if cell.type == self.STROMA:
                        # FIELD 'F' MUST MATCH THE XML CHEMICAL FIELD NAME
                                cd = self.chemotaxisPlugin.addChemotaxisData(cell, "EPIgrad")      #ECGRAD CHANGED TO EPIGRAD 
                                cd.setLambda(2.0)
                                cd.assignChemotactTowardsVectorTypes([self.EPI, self.MEDIUM, self.ECM])
                            

                # print("Turning ON chemotaxis at MCS =", mcs)
        
                # APPLYING LAMBDA TO ALL CELLS OF A GIVEN TYPE
                for cell in self.cell_list:
                        if cell.type == self.STROMA:
                                if 250 < cell.yCOM < 264:
                                        if int(cell.yCOM) in self.muscle_fold_coordinates:               ## HERE WE ARE SPECIFYING THE COORDS OF STROMAL CELLS TO RESPOND TO CHEMOTAXIS 
                                                # print("the values are:", int(cell.yCOM))
                                        
                                                cd = self.chemotaxisPlugin.getChemotaxisData(cell, "EPIgrad")   #ECGRAD CHANGED TO EPIGRAD
                                                if cd:
                                                        lm = cd.getLambda()
                                                        cd.setLambda(lm)
                                            
                
        
        
        
        if mcs%100==0 and mcs<4000:
            
            
                for cell in self.cell_list_by_type(self.EPI, self.ECM):
                    
                        direction = (cell.xCOM-(self.dim.x/2))/(self.dim.x/2)
                        if cell.xCOM < temp[0] or cell.xCOM > temp[-1]:    
                                cell.lambdaVecX = direction*0.5  # FORCE COMPONENT POINTING ALONG X AXIS - TOWARDS POSITIVE X'S
                    # MAKE SURE EXTERNALPOTENTIAL PLUGIN IS LOADED
                        else: 
                                cell.lambdaVecX = direction*-0.5 
                
                
        if mcs>=4000 and mcs%100==0:
                for cell in self.cell_list_by_type(self.EPI, self.ECM):
                
                        direction = (cell.xCOM-(self.dim.x/2))/(self.dim.x/2)
                
                        # ASSIGN FORCE DIRECTION BASED ON LOCATION OF CELL
                        if cell.xCOM < temp[0] or cell.xCOM > temp[-1]:
                                cell.lambdaVecX = direction*1.0  # FORCE COMPONENT POINTING ALONG X AXIS - TOWARDS POSITIVE X'S  
                        else:
                                cell.lambdaVecX = direction*-1.0    
                   
         
      
        # ASSIGNING FORCE GRADIENT TO THE STROMA 
            
        if mcs>=4000 and mcs%100==0:
                A = temp   # EXAMPLE: FOLD COORDINATE LIST

                # APPLY X-DIRECTION FORCES (SAME AS BEFORE)
                for cell in self.cell_list_by_type(self.STROMA):
                        direction = (cell.xCOM - (self.dim.x / 2)) / (self.dim.x / 2)

                        if cell.xCOM < A[0] or cell.xCOM > A[-1]:
                            cell.lambdaVecX = direction * 0.5
                        else:
                            cell.lambdaVecX = direction * -0.5

                

            
                F0 = self.stromaCell_force                              # BASE (PEAK) LAMBDAVECY AT A FOLD CENTER
                decay_rate = self.stromaDecay                           # EXPONENTIAL DECAY RATE (LARGER -> FASTER DECAY)
                fold_centers = self.muscle_fold_coordinates             # X POSITIONS OF THE TWO FOLD CENTERS. USING MUSCLE CORRDINATES TO FOLD THE STROMAL LAYER 
                apply_halfwidth = 120.0                                 # OPTIONAL: ONLY APPLY FORCE IF ABS(DX) < APPLY_HALFWIDTH
                max_lambda = 200.0                                      # MAX LIMIT FOR THE FORCE STRENGTH

                
                '''
                APPLY Y-DIRECTED FORCES THAT ARE STRONGEST AT EACH X IN FOLD_CENTERS AND
                DECAY AWAY EXPONENTIALLY. CELLS ABOVE CENTER_Y ARE PULLED DOWNWARD;
                CELLS BELOW ARE PULLED UPWARD (SO TISSUE BENDS INWARD).
                '''

                center_y = self.dim.y / 2.0                                # CENTER OF Y AXIS 

                # PRECOMPUTE: KEEP FOLD CENTERS AS FLOATS
                centers = [float(c) for c in fold_centers]                 # CONVERTING EVERY FOLD CENTER COORDINATE TO FLOAT FOR CONSISTENCY.

                # ITERATE OVER STROMAL CELL LIST 
                for cell in self.cell_list_by_type(self.STROMA):  
                    xcell = float(cell.xCOM)   #KEEPING ALL THE X CORRDINATES OF THE CELL IN DECIMAL
                    ycell = float(cell.yCOM)   #KEEPING ALL THE Y CORRDINATES OF THE CELL IN DECIMAL

                    # COMPUTE COMBINED CONTRIBUTION FROM BOTH FOLD CENTERS
                    Fy = 0.0
                    for cx in centers:                                        # CELLS FEEL FORCE FROM EACH FOLD SIMULTANEOUSLY.
                        dx = abs(xcell - cx)                                  # DISTANCE FROM FOLD CENTER → CONTROLS EXPONENTIAL DECAY.
                        # OPTIONALLY SKIP FAR AWAY TO SAVE COMPUTE AND AVOID TINY FORCES
                        if dx <= apply_halfwidth:                             # IF THE CELL IS FARTHER THAN ±120 PIXELS, SKIP FORCE CONTRIBUTION.
                            Fy += F0 * math.exp(-decay_rate * dx)             # MAIN DECAY EQUATION 

                    # CLAMP / SAFETY
                    if Fy > max_lambda:
                        Fy = max_lambda                # SAFETY: AVOID OVERLY LARGE FORCES.

                    # IF FORCE IS EXTREMELY TINY, ZERO IT OUT (OPTIONAL)
                    if Fy < 1e-6:
                        cell.lambdaVecY = 0.0
                        # OPTIONALLY CLEAR TARGETVECY TOO
                        # cell.targetVecY = 0.0
                        continue

                    # CHOOSE DIRECTION: CELLS ABOVE CENTER_Y SHOULD MOVE DOWN, BELOW MOVE UP
                    # WE SET TARGETVECY TO -1.0 (DOWN) IF YCELL > CENTER_Y, ELSE +1.0 (UP).
                    # THIS ENSURES THE SIGN/DIRECTON IS CORRECT; LAMBDA IS MAGNITUDE.
                    if ycell > center_y:
                        cell.targetVecY = -1.0
                    else:
                        cell.targetVecY = +1.0

                    # APPLY MAGNITUDE
                    cell.lambdaVecY = Fy

                    # OPTIONALLY SET TARGETVECX TO 0 TO AVOID ACCIDENTAL X BIAS
                    cell.targetVecX = 0.0
                    
                    if mcs >= 5600:
                        cell.lambdaVecY = 0.0
                
            
            
        # ASSIGNING THE FORCE GRADIENT TO THE MUSCLES    
        if mcs>=4000 and mcs%100 == 0:
            F0 = self.muscleCell_force                               # BASE (PEAK) LAMBDAVECY AT A FOLD CENTER
            decay_rate = self.muscleDecay                            # EXPONENTIAL DECAY RATE (LARGER -> FASTER DECAY)
            fold_centers = self.muscle_fold_coordinates              # X POSITIONS OF THE TWO FOLD CENTERS (EXAMPLE)
            apply_halfwidth = 120                                    # OPTIONAL: ONLY APPLY FORCE IF ABS(DX) < APPLY_HALFWIDTH
            max_lambda = 200.0                                       # MAX LIMIT FOR THE FORCE STRENGTH

            
            '''
            APPLY Y-DIRECTED FORCES THAT ARE STRONGEST AT EACH X IN FOLD_CENTERS AND
            DECAY AWAY EXPONENTIALLY. CELLS ABOVE CENTER_Y ARE PULLED DOWNWARD;
            CELLS BELOW ARE PULLED UPWARD (SO TISSUE BENDS INWARD).
            '''

            center_y = self.dim.y / 2.0                # FETCH THE CENTER OF Y-AXIS 

            # PRECOMPUTE: KEEP FOLD CENTERS AS FLOATS(DECIMAL)
            centers = [float(c) for c in fold_centers]

            # ITERATE OVER MUSCLE CELL LIST
            
            for cell in self.cell_list_by_type(self.MUSCLE):  
                xcell = float(cell.xCOM)
                ycell = float(cell.yCOM)

                # COMPUTE COMBINED CONTRIBUTION FROM BOTH FOLD CENTERS
                Fy = 0.0                 # INITIATING THE VALUES
                for cx in centers:
                    dx = abs(xcell - cx)
                    # OPTIONALLY SKIP FAR AWAY TO SAVE COMPUTE AND AVOID TINY FORCES
                    if dx <= apply_halfwidth:
                        Fy += F0 * math.exp(-decay_rate * dx)   #FY = F0*E(-DECAY_RATE * DX)
                        # DECAY RATE CONTROLS HOW FAST THE VALUE CHANGES
                        # WHEN DX = 0 --- FY = F0   HIGHEST IN THE MIDDLE 
                        # AS DX INCREASES, FY APPROACHES 0
                        # LARGER DECAY ---- FASTER DROP OFF. 

                # CLAMP / SAFETY
                if Fy > max_lambda:
                    Fy = max_lambda

                # IF FORCE IS EXTREMELY TINY, ZERO IT OUT 
                if Fy < 1e-6:
                    cell.lambdaVecY = 0.0
                    # OPTIONALLY CLEAR TARGETVECY TOO
                    # cell.targetVecY = 0.0
                    continue

                # CHOOSE DIRECTION: CELLS ABOVE CENTER_Y SHOULD MOVE DOWN, BELOW MOVE UP
                # WE SET TARGETVECY TO -1.0 (DOWN) IF YCELL > CENTER_Y, ELSE +1.0 (UP).
                # THIS ENSURES THE SIGN/DIRECTON IS CORRECT; LAMBDA IS MAGNITUDE.
                if ycell > center_y:
                    cell.targetVecY = -1.0
                else:
                    cell.targetVecY = +1.0

                # APPLY MAGNITUDE
                cell.lambdaVecY = Fy

                # OPTIONALLY SET TARGETVECX TO 0 TO AVOID ACCIDENTAL X BIAS
                cell.targetVecX = 0.0
                    
                if mcs >= 5600:
                        cell.lambdaVecY = 0.0
       
       
           
        
        
        pass
        
        
#==========================================================================     
##IN THIS CLASS, APPLYTING MITOSIS TO MUSCLE CELLS AT THE POINT OF BREAK ##
#==========================================================================


#If I try to get the fetch the cells by coordinates then it would be cheating. I have to code it in a way that it can somehow sense or somehow
#we can be able to calculate the dimensions of the cells and when the dimension of the things and gets above a certain limit we can run the mitosis function 

        
class MuscleCellMitosis(MitosisSteppableBase):
    def __init__(self, frequency=1):
        MitosisSteppableBase.__init__(self, frequency)

        
        self.set_parent_child_position_flag(0)
        
        
    def start(self):
        self.deformation_counter = {}


    def step(self, mcs):
        
        
        
        
        if 100 < mcs <= 3000 and mcs % 750 == 0:
                if mcs > 3000:
                    return
                    
                    
                else:
                    muscle_cells = [cell for cell in self.cell_list if cell.type == self.MUSCLE]
                    

                    if not muscle_cells:
                        return

                # choose ONE random muscle cell
                    
                    
                    chosen_cell = random.choice(muscle_cells)

                # trigger mitosis
                    self.divide_cell_random_orientation(chosen_cell) 
                    
                    
                    
                    
                    
                    def update_attributes(self):               # UPDATING THE TYPE OF CELLS THAT WILL FORM AFTER MITOSIS

                        # REDUCE PARENT TARGET VOLUME BEFORE CLONING
                        self.parent_cell.targetVolume /= 2.0

                        self.clone_parent_2_child()

                        # MAKE THE CELL TYPE CHANGE EVERY TIME THE CELL DIVIDES
                        if self.parent_cell.type == self.MUSCLE:
                            self.child_cell.type = self.MUSCLE
                        else:
                            self.child_cell.type = self.CONDENSING
                
        if mcs > 3000 and mcs % 50 == 0:
                
                if mcs > 4000:
                    return
               
            
                else:
                    stroma_cells = [cell for cell in self.cell_list if cell.type == self.STROMA]
                
                    if not stroma_cells:
                        return 
                    
                    
                    cell_to_divide = random.choice(stroma_cells)
                
                    self.divide_cell_random_orientation(cell_to_divide)
                        
                        
                        
                    
                    

                    def update_attributes(self):               # UPDATING THE TYPE OF CELLS THAT WILL FORM AFTER MITOSIS

                        # REDUCE PARENT TARGET VOLUME BEFORE CLONING
                        self.parent_cell.targetVolume /= 2.0

                        self.clone_parent_2_child()

                        # MAKE THE CELL TYPE CHANGE EVERY TIME THE CELL DIVIDES
                        if self.parent_cell.type == self.STROMA:
                            self.child_cell.type = self.STROMA
                        else:
                            self.child_cell.type = self.NEWTYPE
                      
                
                
                
        # import math

        # ASPECT_THRESHOLD = 2.5
        # PERSISTENCE_MCS = 200
        
        
        # def periodic_length(coords, L):
            # coords = sorted(coords)
            # gaps = []

            # for i in range(len(coords) - 1):
                # gaps.append(coords[i+1] - coords[i])

            # # gap across periodic boundary
            # gaps.append((coords[0] + L) - coords[-1])

            # return L - max(gaps)

        
        
        
        # if mcs > 100 and mcs%100 == 0:
            
            
            # for cell in self.cellList:
                # if cell.type != self.MUSCLE:
                    # continue

                # Ixx, Iyy, Ixy = cell.iXX, cell.iYY, cell.iXY

                # trace = Ixx + Iyy
                # det = Ixx*Iyy - Ixy*Ixy

                # lambda1 = trace/2 + ((trace**2)/4 - det)**0.5
                # lambda2 = trace/2 - ((trace**2)/4 - det)**0.5

                # if lambda2 <= 0:
                    # continue

                # major = math.sqrt(lambda1)
                # minor = math.sqrt(lambda2)

                # aspect_ratio = major / minor

                # # initialize memory
                # if cell.id not in self.deformation_counter:
                    # self.deformation_counter[cell.id] = 0

                # if aspect_ratio > ASPECT_THRESHOLD:
                    # self.deformation_counter[cell.id] += 1
                # else:
                    # self.deformation_counter[cell.id] = 0

                # if self.deformation_counter[cell.id] >= PERSISTENCE_MCS:
                    # self.divide_cell_random_orientation(cell)
                    # self.deformation_counter[cell.id] = 0
                    
                    
                # def update_attributes(self):               # UPDATING THE TYPE OF CELLS THAT WILL FORM AFTER MITOSIS

                # # REDUCE PARENT TARGET VOLUME BEFORE CLONING
                    # self.parent_cell.targetVolume /= 2.0

                    # self.clone_parent_2_child()

                    # # MAKE THE CELL TYPE CHANGE EVERY TIME THE CELL DIVIDES
                    # if self.parent_cell.type == self.MUSCLE:
                        # self.child_cell.type = self.MUSCLE
                    # else:
                        # self.child_cell.type = self.CONDENSING        

            
            # len_x =[]
            # len_y = []
            
            
            # for cell in self.cellList:
                # if cell.type != self.MUSCLE:
                    # continue

                # Ixx = cell.iXX
                # Iyy = cell.iYY
                # Ixy = cell.iXY

                # trace = Ixx + Iyy
                # det = Ixx*Iyy - Ixy*Ixy

                # lambda1 = trace/2 + ((trace**2)/4 - det)**0.5
                # lambda2 = trace/2 - ((trace**2)/4 - det)**0.5

                # major_axis = (lambda1)**0.5
                # minor_axis = (lambda2)**0.5
                
                # len_x.append(major_axis)
                # len_y.append(minor_axis)
                
                
            # print("weuvwuevceuwvcweucvweucvweucvwucweucvweugcvewcgwev", len_x)    
            
            
            # Lx = self.dim.x
            # Ly = self.dim.y

            # listx, listy = [], []

            # for cell in self.cellList:
                # if cell.type != self.MUSCLE or cell.id == 0:
                    # continue

                # xs, ys = [], []

                # for pixel in self.getCellPixelList(cell):
                    # xs.append(pixel.pixel.x)
                    # ys.append(pixel.pixel.y)
                # print("this is wqndewfbeuwfbeuwfbewucb", xs)

                # if not xs:
                    # continue

                # lx = periodic_length(xs, Lx)
                # ly = periodic_length(ys, Ly)

                # listx.append(lx)
                # listy.append(ly)

            # print("listx:", listx)
            # print("listy:", listy)

            
            
            
        
            # listx, listy = [], []

            # for cell in self.cellList:
                # if cell.type != self.MUSCLE or cell.id == 0:
                    # continue

                # xs, ys = [], []

                # for pixel in self.getCellPixelList(cell):
                    # xs.append(pixel.pixel.x)
                    # ys.append(pixel.pixel.y)

                # if not xs:
                    # continue

                # lx = max(xs) - min(xs) + 1
                # ly = max(ys) - min(ys) + 1

                # listx.append(lx)
                # listy.append(ly)

            # print("listx:", listx)
            # print("listy:", listy)
            
            
            # listx = []
            # listy = []
            
            

            # for cell in self.cellList:
                # xs, ys = [], []
                
                # if cell.type == self.MUSCLE:
                    # for pixel in self.getCellPixelList(cell):
                        # # print("this is the structure:",len(str(self.getCellPixelList(cell))))
                        # xs.append(pixel.pixel.x)
                        # ys.append(pixel.pixel.y)

                    # lx = max(xs) - min(xs) 
                    # ly = max(ys) - min(ys) 
                    
                    
                    # listx.append(lx)
                    # listy.append(ly)
                
            # print("listx is the following", listx, "\nlisty is the following", listy )        
        
        # for cell in self.cellList:
            # if cell.type == 4:
                # pixel_list = self.get_cell_pixel_list(cell)
                # for pixel_tracker_data in pixel_list:
                    # print("pixel of cell id=", cell.id, " type:", cell.type, " = ", pixel_tracker_data.pixel,
                          # " number of pixels=", pixel_list.number_of_pixels())
                          
                          
        # output_path = os.path.join(self.output_dir, "pixel_track.txt")

        # with open(output_path, "w") as f:
    # # CSV header
            # f.write("cell_id,cell_type,x,y,z,no_pixels\n")

            # for cell in self.cellList:
                # if cell.type == 4:
                    # pixel_list = self.get_cell_pixel_list(cell)
                    # num_pixels = pixel_list.number_of_pixels()
                    
                    # count = 0
                    
                    # for pixel_tracker_data in pixel_list:
                        # count += 1
                        
                    # cc3d_count = pixel_list.number_of_pixels()
                    
                    
                
                
                    # print(
                        # "Cell ID:", cell.id,
                        # "Type:", cell.type,
                        # "Manual pixel count:", count,
                        # "CC3D pixel count:", cc3d_count
                        # )    

                    # for pixel_tracker_data in pixel_list:
                        # count += 1
                        
                        # x = pixel_tracker_data.pixel.x
                        # y = pixel_tracker_data.pixel.y
                        # z = pixel_tracker_data.pixel.z

                        # f.write(f"{cell.id},{cell.type},{x},{y},{z},{num_pixels}\n")            

        
        # xs, ys = [], []

        # for cell in self.cellList:
            # if cell.type == self.MUSCLE:
                # for px in self.getCellPixelList(cell):
                    # xs.append(px.x)
                    # ys.append(px.y)

                # lx = max(xs) - min(xs) + 1
                # ly = max(ys) - min(ys) + 1
            
                # print(cell.id, lx, ly)

        



            # cell_to_divide_stretch = []
            # for cell in self.cell_list_by_type(self.MUSCLE):
                # if 
           
            # ##NOT STRESS BASED MITOSIS
            # cells_to_divide = []                   #STORING ALL THE CORRDINATES OF MUSCLE CELLS TO DIVIDE
            # for cell in self.cell_list:
                # if cell.type == self.MUSCLE:
                    # if 300 < cell.xCOM < 450:      # SPECIFYING THE COORDINATES OF THE MUSCLE CELLS 
                        # if cell.volume >= 2500:    # IF VOLUME IS MORE THAN OR EQUAL TO 2500 THEN DIVIDE 
                            # cells_to_divide.append(cell)

            # for cell in cells_to_divide:
                
                # self.divide_cell_random_orientation(cell)  # DIVIDE IN A RANDOM ORIENTATION
                
                
                
        # if mcs % 500 == 0:
            
                    # muscle_cells = [cell for cell in self.cell_list if cell.type == self.MUSCLE]

                    # if not muscle_cells:
                        # return

                # # choose ONE random muscle cell
                    # chosen_cell = random.choice(muscle_cells)

                # # trigger mitosis
                    # self.divide_cell_random_orientation(chosen_cell)        
                
                

            # def update_attributes(self):               # UPDATING THE TYPE OF CELLS THAT WILL FORM AFTER MITOSIS

                # # REDUCE PARENT TARGET VOLUME BEFORE CLONING
                # self.parent_cell.targetVolume /= 2.0

                # self.clone_parent_2_child()

                # # MAKE THE CELL TYPE CHANGE EVERY TIME THE CELL DIVIDES
                # if self.parent_cell.type == self.MUSCLE:
                    # self.child_cell.type = self.MUSCLE
                # else:
                    # self.child_cell.type = self.CONDENSING       
      
     
        
        
        
        
        
        

  
