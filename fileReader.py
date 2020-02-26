from celestialBody import celestialBody
from celestialSystem import orbitalMotion

class fileReader(object):
    """File reader class to read in parameters from files and pass
    them to orbitalMotion object"""
    def __init__(self,path):
        """Constructor of file reader taking file name as argument"""
        self.file = open(path,'r')
        self.args = self.file.readlines()
    
    def create(self):
        """Read in arguments in the corresponding file 
        and create an object of orbitalMotion"""

        """read in the first line of arguments as basic setting of animation"""
        simArgs = self.args[0].split()  
        timeStep = (int)(simArgs[0])
        if len(simArgs) > 1:
            iterTimes = simArgs[1]
        else: 
            iterTimes = 500
        
        """Read in arguments from other lines as parameters of each planet"""
        bodies = []
        for i in range(1, len(self.args)):
            args = self.args[i].split()
            name = args[0]
            mass = (float)(args[1])
            x = (float) (args[2])
            y = (float)(args[3])
            radius = (float)(args[4])
            if len(args) > 5 :
                color = args[5]
            else: 
                color = 'violet'
            newBody = celestialBody(name,mass,x,y,radius,color)  #generate a new celestial body object
            bodies.append(newBody)
        
        """The first line arguments are those of the center body
        while others are bodies orbiting around it"""
        model = orbitalMotion(bodies[0],bodies[1:],timeStep,iterTimes)
        return model

def main():
    reader = fileReader('C:\\Users\\12639\\ComputerSimulation\\OrbitalMotion SecEdi\\Argument.txt')
    model = reader.create()
    model.run()

if __name__ == '__main__':
    main()