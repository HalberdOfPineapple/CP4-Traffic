import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
from celestialBody import celestialBody

class orbitalMotion(object):
    def __init__(self,star,planets,timeStep,iterTimes = 500):
        """Constructor of the simulator, taking star(center body) as the first parameter, a list
        of orbiting bodies, timeStep, iterationTimesto be other parameters"""
        self.star = star
        self.bodies = planets
        self.bodies.append(star)  #Making sure the center body is the last one of self.bodies
        self.timeStep = timeStep
        self.iterTimes = iterTimes
        self.initialV()

    def initialV(self):
        """Initializing velocity of each celestial body depending 
        on the formula: v = (GM/r)^(1/2)"""
        for planet in self.bodies[:-1]:
            dx = planet.x - self.star.y
            print(dx)
            dy = planet.y - self.star.y
            print(dy)
            d = math.sqrt(dx**2 + dy**2)
            theta = math.atan2(dy,dx)
            sine = math.sin(theta + math.pi)   #Theta's sine value is the reverse of the standard definition of sine
            cosine = math.cos(theta)
            vi = math.sqrt(celestialBody.G * self.star.mass / d )
            planet.vx = vi * sine
            planet.vy = vi * cosine

    def orbit(self):
        """Method used to update each body's displacement,velocity and accelaration"""
        for ind, body in enumerate(self.bodies):
            body.ax = 0
            body.ay = 0
            body.accelerations(np.delete(self.bodies, ind))
        for body in self.bodies:
            body.updatePosition(self.timeStep)

    def sumEk(self):
        """Method to calculate the total amount of kinetic energy"""
        sum = 0
        for body in self.bodies:
            sum += body.kineticE()
        return sum

    def init(self):
        self.timeText.set_text('')
        return self.patches

    def animate(self,i):
        self.orbit()
        self.timeText.set_text('Total kinetic energy is: ' + str(self.sumEk()))
        for i in range(len(self.bodies)):
            body = self.bodies[i]
            self.patches[i].center = (body.x, body.y) 
        return tuple(self.patches) + tuple([self.timeText])

    def run(self):
        """Running method of the simulation class"""
        limScale = 1.35 * celestialBody.maxRi(self.bodies)
        fig = plt.figure()
        ax = plt.axes()
        self.patches = []

        for i in range(len(self.bodies)):
            body = self.bodies[i]
            self.patches.append(plt.Circle((body.x ,body.y),
            radius = limScale * body.radius / self.bodies[-1].radius /(9 if i !=len(self.bodies)-1 else 5)
            ,color = body.color,animated = True,label = body.name))
            ax.add_patch(self.patches[i])


        ax.set_xlim(-limScale+ self.bodies[-1].x,limScale + self.bodies[-1].x)
        ax.set_ylim(-limScale+ self.bodies[-1].y,limScale + self.bodies[-1].y) #Making sure the center body is in the center of figure
        ax.set_xlabel('y')
        ax.set_ylabel('x')
        self.timeText = ax.text(0.02, 0.95, '', transform=ax.transAxes)        


        # create the animator
        anim = FuncAnimation(fig, self.animate, init_func = self.init,frames = self.iterTimes, repeat = True, interval = 200, blit = True)
        legend = ax.legend(loc= 'upper center', bbox_to_anchor=(0.5, 1.1), ncol=len(self.bodies))

        # plt.grid()
        ax.set_aspect('equal') # Making sure the scale of 2 axes are equal

        plt.show()

def main():
    mars = celestialBody('Mars',6.4185e23,0,0,6)
    r12 = 9.3773e6
    r13 = 2.346e7
    phobos = celestialBody('Phobos',1.06e16,r12,0,2,'r')
    deimos = celestialBody('Deimos',1.47e15,-r13,0,1.5,'b')
    planets = [phobos,deimos]
    model = orbitalMotion(mars,planets,10)
    model.run()

if __name__ == '__main__':
    main()
    
    
