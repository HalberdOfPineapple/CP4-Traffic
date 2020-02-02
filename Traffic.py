import random as random

class road(object):
    def __init__(self,length,density):
        self.cells = [0] * length
        self.cars = round(density * length)
        self.avg_speed = []
        random_cells = []
        for i in range(0,length):
            exists = True
            while exists:
                rand = random.random()
                exists = random_cells.count(rand) > 0 
            random_cells.append(rand)
            self.cells[(int)(rand*(length-1))] = 1
    
    def move(self):
        if self.cars == 0:
            return 0
        else:
            next = self.cells.copy()
            move = 0
            for i in range(0,len(self.cells)):
                if i == len(self.cells)-1 :
                    if self.cells[i] == 1:
                        if self.cells[0] == 1 :
                            next[i] = 1
                        else:
                            next[i] = 0
                            move += 1
                    elif self.cells[i] == 0:
                        if self.cells[i-1] == 1:
                            next[i] = 1
                            move += 1
                        else:
                            next[i] = 0
                elif i == 0:
                    if self.cells[i] == 1:
                        if self.cells[i+1] == 1 :
                            next[i] = 1
                        else:
                            next[i] = 0
                            move += 1
                    elif self.cells[i] == 0:
                        if self.cells[len(self.cells)-1] == 1:
                            next[i] = 1
                            move += 1
                        else:
                            next[i] = 0
                else:
                    if self.cells[i] == 1:
                        if self.cells[i+1] == 1 :
                            next[i] = 1
                        else:
                            next[i] = 0
                            move += 1
                    elif self.cells[i] == 0:
                        if self.cells[i-1] == 1:
                            next[i] = 1
                            move += 1
                        else:
                            next[i] = 0
            self.cells = next
            self.avg_speed.append(move/self.cars)
            return move

    
    def iterate(self,iterTimes):
        for i in range(0,iterTimes):
            self.move()

    def printRoad(self):
        print(' '.join(map(str,self.cells)))

    def timePrint(self,times):
        self.printRoad()
        for i in range(0,times):
            self.move()
            self.printRoad()

    def steadyAvgSpeed(self):
        if (self.cars == 0):
            return 0
        else:
            control = False
            while not control:
                self.iterate(2)
                control = self.avg_speed[-1] == self.avg_speed[-2]
            return self.avg_speed[-1]

    
    @classmethod
    def calSteadyAvgSpeed(cls,length,density):
        temp = road(length,density)
        return temp.steadyAvgSpeed()


def main():
    # r = road(40,0.22)
    # r.timePrint(10)
    # print(' '.join(map(str,r.avg_speed)))
    # print(r.steadyAvgSpeed())
    print(road.calSteadyAvgSpeed(40,0.22))

main()

    # def avgSpeed(self,iterTimes):
    #     for i in range(0,iterTimes):
    #         avg_speed.append(self.move()/self.cars)
    #     return avg_speed

    
    # def steadyAvgSpeed(self):
    #     control = False
    #     while not control:
    #         avg_speed = self.avgSpeed(i)
    #         i += 1
    #         control = avg_speed[-1] == avg_speed[-2]
    #     return avg_speed[-1]
        # @staticmethod
    # def steadyAvgSpeedTest(density,length = 40):
    #     r = road(length,density)
    #     return r.steadyAvgSpeed()