import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Traffic import road


class TrafficAnimation(object):
    HEIGHT = 50 #Setting the height of graph

    def __init__(self,length,density,iterTimes = 500):
        """Initialize the road's length and density, setting 
        final x coordinate to be the length of the road"""
        # set initial and final x coordinates of the graph
        self.xpos = 0.0
        self.xmax = length
        
        self.iter = iterTimes             #Setting the number of frames

        self.r = road(length,density)     # initialize a road object 

    def init(self):
        """initialiser for animator"""
        self.timeText.set_text('')
        return self.patches

    def animate(self, i):
        """method for iterating to be used in the animator"""
        self.r.move()
        self.timeText.set_text('The average speed is '+str(self.r.avg_speed[-1])+'\nIteration times: ' + str(i))
        for j in range(0,len(self.r.cells)):
            self.patches[j].set_height(0.5 * TrafficAnimation.HEIGHT * self.r.cells[j])
        return tuple(self.patches) + tuple([self.timeText])

    def run(self):
        """method for animation running"""

        fig = plt.figure()
        ax = plt.axes()
        height = TrafficAnimation.HEIGHT
        self.patches = []

        """Generating rectangles in each cell where there is a car to represent the state"""
        for i in range(0,len(self.r.cells)):
            self.patches.append(plt.Rectangle((i,0),1,0.5 * TrafficAnimation.HEIGHT * self.r.cells[i],color = 'black',animated = True))
            ax.add_patch(self.patches[i])

        """set up the axes"""
        ax.axis('scaled')
        ax.set_xlim(self.xpos, self.xmax)
        ax.set_ylim(0, height)
        ax.set_xlabel('cells of the road (length = ' + str(len(self.r.cells)) + ', total number of cars = '+ str(self.r.cars)+')' )
        ax.set_ylabel('cars in cells ('+str(0.5*height)+' times of 1 or 0)')
        # initialize the text positions
        self.timeText = ax.text(1,height - min(len(self.r.cells)/10,height/2-2),'',fontsize=7.5)

        # create the animator
        anim = FuncAnimation(fig, self.animate, init_func = self.init, frames = self.iter+1, repeat = False, interval = 200, blit = True)

        # show the plot
        plt.show()

def main():
    s = TrafficAnimation(120,0.5)
    s.run()
    
if __name__ == '__main__':
    main()
