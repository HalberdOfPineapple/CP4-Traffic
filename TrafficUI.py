from Traffic import road
from TrafficAnimation import TrafficAnimation
from TrafficAnimation2 import TrafficAnimation2
from TrafficAvgSpeedAnalyser import avgSpeedAnalyser


"""UI file for presenting traffic simulation"""
try:

    #Taking user input from console
    choice = input("Input your choice:\n" + 
        "1. Analysis of average speed\n" +
        "2. Graphical representation of the road(mode 1)\n" +
        "3. Graphical representation of the road(mode 2)\n" +
        "4. Digital representation of the road\n")

    #Calling average speed analyser to generate corresponding graph
    if (int)(choice) == 1:
        length = (int)(input("Input the length of the road:"))
        avgAlg = avgSpeedAnalyser(length)
        avgAlg.run()

    # Calling corresponding animation generator
    elif (int)(choice) == 2 or (int)(choice) == 3:
        inp = input("Input the length and density (or and the iteration times) of the road: ")
        length = (int)(inp.split()[0])
        density = (float)(inp.split()[1])
        iterTimes = 500 if len(inp.split()) < 3 else  (int)(inp.split()[2])
        animator = TrafficAnimation(length,density,iterTimes) if (int)(choice) == 2 else TrafficAnimation2(length,density,iterTimes)
        animator.run()
    
    elif (int)(choice) == 4:
        inp = input("Input the length and density (or and the iteration times) of the road: ")
        length = (int)(inp.split()[0])
        density = (float)(inp.split()[1])
        iterTimes = 10 if len(inp.split()) < 3 else  (int)(inp.split()[2])
        r = road(length,density)
        r.timePrint(iterTimes)
        
    # case for invalid input
    else:
        print("Invalid choice!")

#Handling exception
except Exception as ex:
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
