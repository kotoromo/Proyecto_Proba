from Distribution import *
from Utilities import Maths

class Bernoulli(Distribution):
    type = "bernoulli"
    START = 1
    success = 0
    failure = 1-success
    x = 0.0

    def __init__(self, success, x):
        self.success = success
        self.failure = 1-self.success
        self.x = x

    def getDistribution(self):
        return (self.success**self.x)*(1-self.success)**1-self.x

    def getMed(self):
        med = self.success

        return med

    def getType(self):
        return self.type

    def getVar(self):
        var = self.success*(1-self.success)
        return var

    def setX(self, X):
        self.X = X

    def setSuccess(self, success):
        self.success = success

