import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from Traffic import road


class TrafficAnimation2(object):
    HEIGHT = 50
    RADIUS = 0.4

    def __init__(self,length,density,iterTimes = 500):
        """set initial and final x coordinates of the graph"""
        self.xpos = 0
        self.xmax = length
        
        """ set number of frames"""
        self.iter = iterTimes

        """initialize a road object""" 
        self.r = road(length,density)

    def init(self):
        """initialiser for animator"""
        self.timeText.set_text('')
        return self.patches

    def animate(self, i):
        """animate function of the animator,used for updating each cell's state"""
        self.r.move()
        self.timeText.set_text('The average speed is '+str(self.r.avg_speed[-1])+'\nIteration times: ' + str(i))
        count = 0 # a counter recording the number of cars or the index of patches
        for j in range(0,self.xmax):
            """Setting circles in the cells where there are cars."""
            if self.r.cells[j] == 1:
                xpos = j
                ypos = 0.5 * TrafficAnimation2.HEIGHT + TrafficAnimation2.RADIUS
                self.patches[count].center = (xpos,ypos)
                count += 1
        return tuple(self.patches) + tuple([self.timeText])

    def run(self):
        """Method to generatate the animation"""

        """Initializing the figure, axes and patches"""
        fig = plt.figure()
        ax = plt.axes()
        self.patches = []

        height = TrafficAnimation2.HEIGHT
        radius = TrafficAnimation2.RADIUS

        """Initializing circles in cells where there are cars"""
        for i in range(0,self.xmax):
            if self.r.cells[i] == 1:
                newCircle = plt.Circle((i,0.5 * height + radius),radius,color = 'r',animated = True)
                self.patches.append(newCircle)
                ax.add_patch(newCircle)
        
        """Create a base rectangle in the bottom of the figure"""
        baseRec = plt.Rectangle((0,0),self.xmax,0.5 * TrafficAnimation2.HEIGHT,color = 'b',animated = None)
        ax.add_patch(baseRec)

        """ set up the axes"""
        ax.axis('scaled')
        ax.set_xlim(self.xpos, self.xmax)
        ax.set_ylim(0, height)
        ax.set_xlabel('cells of the road (length = ' + str(len(self.r.cells)) + ', total number of cars = '+ str(self.r.cars)+')' )
        ax.set_ylabel('cars in cells ('+str(0.5*height)+' times of 1 or 0)')
        self.timeText = ax.text(1,height - min(len(self.r.cells)/10,height/2-2),'',fontsize=7.5)

        """create the animator"""
        anim = FuncAnimation(fig, self.animate, init_func = self.init, frames = self.iter+1, repeat = False, interval = 200, blit = True)

        """ show the plot """
        plt.show()

