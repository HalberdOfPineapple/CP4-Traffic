import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Traffic import road


class TrafficAnimation(object):
    HEIGHT = 50

    def __init__(self,length,density):
        # set initial and final x coordinates of the graph
        self.xpos = 0.0
        self.xmax = length
        
        # set number of frames
        self.iter = 500

        # initialize a road object 
        self.r = road(length,density)
    def init(self):
        # initialiser for animator
        return self.patches

    def animate(self, i):
        self.r.move()
        for j in range(0,100):
            self.patches[j].set_height(0.5 * TrafficAnimation.HEIGHT * self.r.cells[j])
        return self.patches

    def run(self):

        fig = plt.figure()
        ax = plt.axes()
        self.patches = []


        for i in range(0,100):
            self.patches.append(plt.Rectangle((i,0),1,0.5 * TrafficAnimation.HEIGHT * self.r.cells[i],color = 'r',animated = True))
            ax.add_patch(self.patches[i])

        # set up the axes
        ax.axis('scaled')
        ax.set_xlim(self.xpos, self.xmax)
        ax.set_ylim(0, TrafficAnimation.HEIGHT)
        ax.set_xlabel('cells of the road (length = ' + str(len(self.r.cells)) + ', total number of cars = '+ str(self.r.cars)+')' )
        ax.set_ylabel('cars in cells ('+str(0.5*TrafficAnimation.HEIGHT)+' times of 1 or 0)')

        # create the animator
        anim = FuncAnimation(fig, self.animate, init_func = self.init, frames = self.iter, repeat = True, interval = 200, blit = True)

        # show the plot
        plt.show()

def main():
    s = TrafficAnimation(100,0.35)
    s.run()
    
main()
