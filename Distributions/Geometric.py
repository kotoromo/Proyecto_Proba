from Distribution import *
from Utilities import Maths

class Geometric(Distribution):
    type = "geometric"
    START = 1
    success = 0
    failure = 1-success
    x = 0
    n = 0

    def __init__(self, success, n):
        self.success = Maths.Maths.convertToDecimal(success)
        self.failure = 1-self.success
        self.n = Maths.Maths.convertToDecimal(n)

    def getProbability(self):
        p = self.success
        n = self.n

        return ((1-p)**(n-1))*(p)

    def getDistribution(self): pass

    def getMed(self):
        med = 1.0/self.success


        return med

    def getType(self):
        return self.type

    def getVar(self):
        var = (1-self.success)/(self.success**2)
        return var

    def set_X(self, X):
        self.X = X

    def setSuccess(self, success):
        self.success = success