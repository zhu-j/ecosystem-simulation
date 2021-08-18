# STUDENT NAME
# 260957235 

import random
import matplotlib.pyplot as plt

class Animal:
    
    # Initializer method
    def __init__(self, my_species, row, column):
        """ Constructor method
        Args:
           self (Animal): the object being created
           my_species (str): species name ("Lion" or "Zebra")
           row (int): row for the new animal
           column (int): column for the new animal
        Returns:
           Nothing
        Behavior:
           Initializes a new animal, setting species to my_species
        """               
        self.species = my_species
        self.row = row
        self.col = column
        self.age = 0
        self.time_since_last_meal = 0

    def __str__(self):
        """ Creates a string from an object
        Args:
           self (Animal): the object on which the method is called
        Returns:
           str: String summarizing the object
        """
        s= self.species+" at position ("+str(self.row)+","+str(self.col)+"):, age="+str(self.age)+", time_since_last_meal="+\
           str(self.time_since_last_meal)
        return s
    
    def can_eat(self, other):
        """ Checks if self can eat other
        Args:
           self (Animal): the object on which the method is called
           other (Animal): another animal
        Returns:
           boolean: True if self can eat other, and False otherwise
        """          
        # WRITE YOUR CODE FOR QUESTION 3 HERE
        if self.species == "Lion" and other.species == "Zebra":
            return True
        else:
            return False
            
    def time_passes(self):
        """ Increases age and time_since_last_meal
        Args:
           self (Animal): the object on which the method is called
        Returns:
           Nothing
        Behavior:
           Increments age and time_since_last_meal
        """           
        # WRITE YOUR CODE FOR QUESTION 4 HERE
        self.age +=1
        self.time_since_last_meal +=1
        
    def dies_of_old_age(self):
        """ Determines if an animal dies of old age
        Args:
           self (Animal): the object on which the method is called
        Returns:
           boolean: True if animal dies of old age, False otherwise
        """          
        # WRITE YOUR CODE FOR QUESTION 5 HERE
        #conditions for which each animal dies of old age
        if self.species == "Lion" and self.age >=18:
            return True
        elif self.species =="Zebra" and self.age >=7:
            return True
        return False
    
    def dies_of_hunger(self):
        """ Determines if an animal dies of hunger
        Args:
           self (Animal): the object on which the method is called
        Returns:
           boolean: True if animal dies of hunger, False otherwise
        """           
         # WRITE YOUR CODE FOR QUESTION 6 HERE  
        if self.species =="Lion" and self.time_since_last_meal >= 6:
             return True
        return False
        
    def will_reproduce(self):
        """ Determines if an animal will reproduce this month
        Args:
           self (Animal): the object on which the method is called
        Returns:
           boolean: True if ready to reproduce, False otherwise
        """          
        # WRITE YOUR CODE FOR QUESTION 7 HERE
        if self.species =="Lion" and self.age in (7,14):
            return True
        elif self.species == "Zebra" and self.age in (3,6):
            return True
        return False
    # end of Animal class
    
def initialize_population(grid_size):
    """ Initializes the grid by placing animals onto it.
    Args:
       grid_size (int): The size of the grid
    Returns:
       list of animals: The list of animals in the ecosystem
    """     
    all_animals=[]
    all_animals.append(Animal("Lion",3,5))
    all_animals.append(Animal("Lion",7,4))
    all_animals.append(Animal("Zebra",2,1))     
    all_animals.append(Animal("Zebra",5,8))
    all_animals.append(Animal("Zebra",9,2))
    all_animals.append(Animal("Zebra",4,4))
    all_animals.append(Animal("Zebra",4,8))
    all_animals.append(Animal("Zebra",1,2))
    all_animals.append(Animal("Zebra",9,4))
    all_animals.append(Animal("Zebra",1,8))
    all_animals.append(Animal("Zebra",5,2))
   
    return all_animals
               

def print_grid(all_animals, grid_size):
    """ Prints the grid
    Args:
       all_animals (list of animals): The animals in the ecosystem
       grid_size (int): The size of the grid
    Returns:
       Nothing
    Behavior:
       Prints the grid
    """   
    
    #get the set of tuples where lions and zebras are located
    lions_tuples = { (a.row,a.col) for a in all_animals if a.species=="Lion"}
    zebras_tuples = { (a.row,a.col) for a in all_animals if a.species=="Zebra"}

    print("*"*(grid_size+2))
    for row in range(grid_size):
        print("*",end="")
        for col in range(grid_size):
            if (row,col) in lions_tuples:
                print("L",end="")
            elif (row,col) in zebras_tuples:
                print("Z",end="")
            else:
                print(" ",end="")
        print("*")
    print("*"*(grid_size+2))


def sort_animals(all_animals):
    """ Sorts the animals, left to right and top to bottom
    Args:
       all_animals (list of animals): The animals in the ecosystem
    Returns:
       Nothing
    Behavior:
       Sorts the list of animals
    """   
    def get_key(a):
        return a.row+0.001*a.col
    all_animals.sort(key=get_key)
    
    
def my_random_choice(choices):
    """ Picks ones of the elements of choices
    Args:
       choices (list): the choices to choose from
    Returns:
       One of elements in the list
    """
    if not choices:
        return None
    
    # for debugging purposes, we use this fake_random_choice function
    def getKey(x):
        return x[0]+0.001*x[1]
    return min(choices, key=getKey)    

    # for actual random selection, replace the above this:
    #return random.choice(choices)


def list_neighbors(current_row, current_col, grid_size):
    """ Produces the list of neighboring positions
    Args:
       current_row (int): Current row of the animal
       current_col (int): Current column of the animal
       grid_size (int): The size of the gride
    Returns:
       list of tuples of two ints: List of all position tuples that are 
                                   around the current position, without 
                                   including positions outside the grid
    """

    all_pos = []
    #iterate through all the possible adjacent cells
    for i in (-1,0,1):
        for j in (-1,0,1):
            #make sure the corrdinates found is not that of the current coordinates
            if i !=0 or j !=0:
                #x and y coordinate of neighbouring cell
                x = current_row +i
                y = current_col +j
                if x in range(grid_size): #coordinates valid only if it's in the grid
                    if y in range(grid_size):
                        tuple_pos = (x,y)
                        all_pos.append(tuple_pos)
    return all_pos
            
                           
def random_neighbor(current_row, current_col,grid_size, only_empty=False, animals=[]):
    """ Chooses a neighboring positions from current position
    Args:
       current_row (int): Current row of the animal
       current_col (int): Current column of the animal
       size (int): Size of the grid
       only_empty (boolean): keyword argument. If True, we only consider 
                             neighbors where there is not already an animal
       animals (list): keyword argument. List of animals present in the ecosystem
    Returns:
       tuple of two int: A randomly chosen neighbor position tuple

    """   
    # WRITE YOUR CODE FOR QUESTION 2 HERE
    neighbouring = list_neighbors(current_row, current_col, grid_size)
    full_neighbours = []
    if only_empty == True:
        for cell in neighbouring: #for each possible neighbouring coordinate 
            for animal in animals:#check if it's in list of coordinates occupied by an animal
                if cell[0] == animal.row and cell[1] == animal.col:
                    tuple_cell = (cell[0],cell[1])
                    full_neighbours.append(tuple_cell)
        for item in full_neighbours: #remove full coordinates from list of possible coordinates
            neighbouring.remove(item)
    random_cell = my_random_choice(neighbouring)
    return random_cell
        


def one_step(all_animals, grid_size):
    """ simulates the evolution of the ecosystem over 1 month
    Args:
       all_animals (list of animals): The animals in the ecosystem
       grid_size (int): The size of the grid
    Returns:
       list fo str: The events that took place
    Behavior:
       Updates the content of animal_grid by simulating one time step
    """  
    events = []    
    sort_animals(all_animals) # ensures that the animals are listed 
                               # from left to right, top to bottom
    # WRITE YOUR CODE FOR QUESTION 8 HERE     
    die_old = []
    die_hunger = []
    eaten = []
    # run time_passes on all animals
    for animal in all_animals:
        animal.time_passes()
        
    # make animals die of old age
    for animal in all_animals:
        if animal.dies_of_old_age()==True:
            die_old.append(animal)
            events.append(str(animal.species) + " dies of old age at position " + str(animal.row) +" "+ str(animal.col))
    for death in die_old:
        all_animals.remove(death)
            
    # make animals die of hunger
    for animal in all_animals:
        if animal.dies_of_hunger() == True:
            die_hunger.append(animal)
            events.append(str(animal.species) + " dies of hunger at position " + str(animal.row) +" "+ str(animal.col))
    for dead in die_hunger:
        all_animals.remove(dead)
        
    # move animals
    for animal in all_animals:
        random_pos = random_neighbor(animal.row, animal.col, grid_size, animals = all_animals)
        #row & col of animal before it moves anywhere
        original_row = animal.row 
        original_col = animal.col
        in_list = False
        index_list = []
        for i, obj in enumerate(all_animals): #check if there's other animals at chosen random position
            if obj.row== random_pos[0] and obj.col ==random_pos[1]:
                index_list.append(i)
                in_list = True
                
        if in_list == True and len(index_list)==1: #execute if there's only one animal with same coordinate 
            other_animal = all_animals[index_list[0]]
            if animal.can_eat(other_animal) == True: #case where the other animal is eaten
                eaten.append(other_animal)
                animal.row = random_pos[0]
                animal.col = random_pos[1]
                animal.time_since_last_meal = 0
                events.append(str(animal.species) + " moves from " + str(original_row) +" "+ str(original_col) + " to " + str(random_pos[0]) +" "+ str(random_pos[1]) + " and eats " + str(other_animal.species))
            elif other_animal.can_eat(animal)==True: #case where the other animal eats the animal that moved
                animal.row = random_pos[0]
                animal.col = random_pos[1]
                other_animal.time_since_last_meal = 0
                eaten.append(animal)
                events.append(str(animal.species) + " moves from " + str(original_row) +" "+ str(original_col) + " to " + str(random_pos[0]) +" "+ str(random_pos[1]) + " and is eaten by " + str(other_animal.species))
        
            elif animal.species == other_animal.species and other_animal not in eaten:
                events.append(str(animal.species) + " tries to move from " + str(original_row) +" "+ str(original_col) + " to " + str(random_pos[0]) +" "+ str(random_pos[1]) + " but square already occupied by same species")
        elif in_list == True and len(index_list)>1:#execute if more than 1 animal with same coordinates
            #more than 1 animal with same coordinates means there has to be 1 lion and multiple zebras that were eaten
            for index in index_list: 
                 other_animal = all_animals[index] 
                 if animal.species == other_animal.species and other_animal in eaten and animal not in eaten:
                        animal.row = random_pos[0]
                        animal.col = random_pos[1]
                        eaten.append(animal)
                        events.append(str(animal.species) + " moves from " + str(original_row) +" "+ str(original_col) + " to " + str(random_pos[0]) +" "+ str(random_pos[1]) + " and is eaten by Lion")
                 elif animal.species == other_animal.species and other_animal not in eaten and animal not in eaten:
                     events.append(str(animal.species) + " tries to move from " + str(original_row) +" "+ str(original_col) + " to " + str(random_pos[0]) +" "+ str(random_pos[1]) + " but square already occupied by same species")
                 else:
                     other_animal.time_since_last_meal = 0 
        elif in_list == False and animal not in eaten: #execute if chosen position is empty
                animal.row = random_pos[0]
                animal.col = random_pos[1]
                events.append(str(animal.species) + " moves from " + str(original_row)+" "+ str(original_col) + " to empty " + str(random_pos[0]) +" "+ str(random_pos[1]))
            
    for animal in eaten: #remove animals that were eaten from list of animals
        all_animals.remove(animal)
    # since animals have moved, we sort the list of animals again, so that
    # we consider them for reproduction in the right order    
    sort_animals(all_animals)
    
    #reproduction of animals
    for parent in all_animals:
        neighbour_pos = random_neighbor(parent.row, parent.col, grid_size,only_empty=True, animals=all_animals)
        #execute if there exist empty neighbouring grids and animal can reproduce
        if neighbour_pos != None and parent.will_reproduce() == True: 
            birth = Animal(my_species=parent.species, row=neighbour_pos[0], column=neighbour_pos[1])
            all_animals.append(birth)
            events.append("Birth of a " + str(birth.species) + " at " + str(birth.row) +" "+ str(birth.col))
    return events
            


def run_whole_simulation(grid_size = 10, simulation_duration = 20, image_file_name="population.png"):
    """ Executes the entire simulation
    Args:
       grid_size (int): Size of the grid
       simulation_duration (int): Number of steps of the simulation
       image_file_name (str): name of image to be created.
    Returns:
       Nothing
    Behavior:
       Simulates the evolution of an animal grid
       Generates graph of species abundance and saves it to populations.png
    """       
    # Do not change this; this initializes the animal population
    all_animals = initialize_population(grid_size)

    # WRITE YOUR CODE FOR QUESTION 9 HERE
    lion = [] #list of number of lions at each point in time
    zebra = []#list of number of zebras at each point in time
    x = range(0,simulation_duration) #x-axis of graph
    for time in range(simulation_duration):
        one_step(all_animals = all_animals, grid_size = grid_size)
        #number of lions and zebras at that time
        lion_num = sum(animal.species=="Lion" for animal in all_animals) 
        zebra_num = sum(animal.species=="Zebra" for animal in all_animals)
        lion.append(lion_num)
        zebra.append(zebra_num)
        
    plt.plot(x, zebra,"r", label = "Zebras") #plot line for zebra
    plt.plot(x, lion,"b",label = "Lions")#plot line for lion
    plt.xlabel("time")
    plt.ylabel("Number of individuals")
    plt.legend(loc = "best")
    plt.savefig("Q9_plot.pdf")

  
    