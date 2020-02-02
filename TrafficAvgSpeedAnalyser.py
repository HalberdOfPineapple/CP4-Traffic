import numpy as np
import matplotlib.pyplot as plt
from Traffic import road

class avgSpeedAnalyser(object):
    def __init__(self,length):
        self.roadLength = length
    
    def run(self):
        vec_avgSpeed = np.vectorize(road.calSteadyAvgSpeed)
        x = np.linspace(0,100,100)
        y = vec_avgSpeed(self.roadLength,x/100)
        plt.plot(x,y)
        plt.title('Average speed of transportation')
        plt.xlabel('Density of traffic')
        plt.ylabel('Average speed')
        plt.show()

def main():
    anal = avgSpeedAnalyser(100)
    anal.run()

main()