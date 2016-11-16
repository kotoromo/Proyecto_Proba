from Distribution import *
from Utilities import Maths

class Geometric(Distribution):
    type = "geometric"
    START = 1
    success = 0
    failure = 1-success
    x = 0
    n = 0

    def __init__(self, success, x, n):
        self.success = success
        self.failure = 1-success
        self.x = x
        self.n = n

    def getDistribution(self):
        return ((1-self.success)**self.n-1)*self.success

    def getMed(self):
        med = 1.0/self.success


        return med

    def getType(self):
        return self.type

    def getVar(self):
        var = (1-self.success)/(self.success**2)
        return var

    def setX(self, X):
        self.X = X

    def setSuccess(self, success):
        self.success = success