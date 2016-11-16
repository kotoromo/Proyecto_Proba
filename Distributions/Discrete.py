from Distribution import *
from Utilities import Maths

class Discrete(Distribution):
    type = "discrete"
    START = 1
    space = 0

    def __init__(self, n):
        self.space = n

    def getDistribution(self):
        return 1.0/float(self.space)

    def getMed(self):
        med = (1.0 / self.space) * Maths.infinite_sum(self.START, self.space, lambda x: x)

        return med

    def getType(self):
        return self.type

    def getVar(self):
        var = (1.0/self.space)* Maths.infinite_sum(self.START, self.space, lambda x: (x-self.getMed())**2 )
        return var

    def setSpace(self):
        self.space = space


if __name__ == '__main__':
    discrete = Discrete(10)
    print (discrete.getMed())
    print (discrete.getVar())
