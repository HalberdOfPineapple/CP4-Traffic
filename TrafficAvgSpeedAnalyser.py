import numpy as np
import matplotlib.pyplot as plt
from Traffic import road

class avgSpeedAnalyser(object):
    def __init__(self,length):
        """Initialize the analyser with the road length"""
        self.roadLength = length
    
    def run(self):
        """Running method of analyser"""
        x = np.linspace(0,1,200)
        y = road.calSteadyAvgSpeed(self.roadLength) #using class method to generate corresponding averafe speed array

        """Setting up the figure"""
        plt.plot(x,y)
        plt.title('Steady average speed of transportation')
        plt.xlabel('Density of traffic (the length of road is ' + str(self.roadLength) +')')
        plt.ylabel('Steady average speed')
        plt.show()

def main():
    asa = avgSpeedAnalyser(150)
    asa.run()

if __name__ == '__main__':
    main()
