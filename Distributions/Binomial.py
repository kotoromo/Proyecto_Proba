from Distribution import *
from Utilities import Maths

class Binomial(Distribution):
    type = "binomial"
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
        return Maths.Combination(self.n, self.x)*(self.success**self.x)*(1-self.success)**self.n-self.x

    def getMed(self):
        med = self.n*self.success


        return med

    def getType(self):
        return self.type

    def getVar(self):
        var = self.n*self.success*(1-self.success)
        return var

    def setX(self, X):
        self.X = X

    def setSuccess(self, success):
        self.success = success