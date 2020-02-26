import numpy as np
import matplotlib as plt
import math

class celestialBody(object):
    G = 6.67408e-11
    def __init__(self,name,mass,x,y,radius,color = 'violet'):
        """Constructor of celestial body taking name, mass, coordinates, radius
        and color as arguments"""
        self.name = name
        self.x = x
        self.y = y
        self.mass = mass
        self.radius = radius
        self.color = color
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 0


    def kineticE(self):
        kE = 0.5 * self.mass * (self.vx ** 2 + self.vy ** 2)
        return kE
    
    def magnitute(self):
        """Method to calculate the distance to the original point"""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def acceleration(self,other):
        """Method to determine the acceleration caused by another celestialbody
        depending on Newton's law"""
        dx = other.x - self.x
        dy = other.y - self.y
        theta = math.atan2(dy,dx)
        r2 = dx ** 2 + dy ** 2
        a = celestialBody.G * other.mass / r2
        self.ax += a * math.cos(theta)
        self.ay += a * math.sin(theta)
        
    
    def accelerations(self,others):
        """Method to determine the acceleration caused by mant bodies"""
        for o in others:
            self.acceleration(o)
        
    
    def updatePosition(self,timeStep):
        """Method to update body's position depending on numerical integration"""
        self.vx += self.ax * timeStep
        self.vy += self.ay * timeStep
        self.x  += self.vx * timeStep
        self.y  += self.vy * timeStep
    
    @classmethod
    def maxRi(cls,bodies):
        """Class method used to calculate the greatest magnitute of a group of bodies"""
        maxR = bodies[0].magnitute()
        for body in bodies:
            if body.magnitute() > maxR:
                maxR = body.magnitute()
        return maxR