import random as random
import numpy as np

class road(object):
    def __init__(self,length,density):
        """Initialize the road's length and density"""
        self.cells =  [0] * length if density != 1 else [1] * length
        self.cars = round(density * length)
        self.avg_speed = []

        if (density <1):
            """Using random method to set cars in random cells"""
            random_cells = []
            while (len(random_cells) != self.cars):
            # for i in range(0,length):
                temp = 0
                exists = True        #Checking whether this random number has been generated
                while exists:        #If so, generate again.
                    rand = (int)(random.uniform(0,1) * (length-1))
                    temp = rand
                    exists = random_cells.count(rand) > 0 
                random_cells.append(temp)
                self.cells[temp] = 1   #Setting the cell selected by random number to be 1(have a car here)
    

    
    def move(self):
        if self.cars == 0 :
            return 0
        next = self.cells.copy()
        move = 0
        length = len(self.cells)
        for i in range(0,length):
            if (self.cells[i] == 1):
                if (self.cells[(i+1)%length] == 0):
                    next[i] = 0
                    move += 1
                elif (self.cells[(i+1)%length] == 1):
                    next[i] = 1
            elif (self.cells[i] == 0):
                if (self.cells[(i-1)%length] == 1):
                    next[i] = 1
                    # move += 1
                elif (self.cells[(i-1)%length] == 0):
                    next[i] = 0
        self.cells = next
        self.avg_speed.append(move/self.cars)
        # print(str(move))
        return move

    
    def iterate(self,iterTimes):
        """method to move the cars in a certain times"""
        for i in range(0,iterTimes):
            self.move()

    def printRoad(self):
        """method to present the distribution of cars in the road"""
        print(' '.join(map(str,self.cells)))

    def timePrint(self,times):
        """Method combining iterate and print road, moving in a certain times with each time 
        printing the road"""
        self.printRoad()
        for i in range(0,times):
            self.move()
            self.printRoad()

    def steadyAvgSpeed(self):
        """Method used to get the road's average moving speed in steady state"""
        if (self.cars == 0):
            return 0  # Without even one car, just return 0
        else:
            control = False
            while not control:
                self.iterate((int)(len(self.cells)/2))                                   # Making sure the cars have moved at least twice
                control = (self.avg_speed[-1] == self.avg_speed[-2] and
                        self.avg_speed[-2] == self.avg_speed[-3] and
                        self.avg_speed[-3] == self.avg_speed[-4] and
                        self.avg_speed[-4] == self.avg_speed[-1]) #checking whether the speed is steady
            return self.avg_speed[-1]

    
    # @classmethod
    # def calSteadyAvgSpeed(cls,length,density):
    #     """Class method used to calculate a road's steady average speed given the length 
    #     and density of the road"""
    #     temp = road(length,density)
    #     return temp.steadyAvgSpeed()
    
    @classmethod
    def calSteadyAvgSpeed(cls,length):
        densities = np.linspace(0,1,200)
        steadyAvg = []
        for x in densities:
            temp = road(length,x)
            steadyAvg.append(temp.steadyAvgSpeed())
        return steadyAvg
