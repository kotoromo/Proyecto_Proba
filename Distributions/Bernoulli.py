from Distribution import *
from Utilities.Maths import Maths

class Bernoulli(Distribution):
    type = "bernoulli"
    START = 1
    success = 0
    failure = 1-success
    x = 0.0

    def __init__(self, success, x):
        self.success = int(success)
        print "success: ", self.success
        self.failure = 1-self.success
        self.x = Maths.convertToDecimal(x)
        print "X", self.x

    def getDistribution(self):
        k = self.success
        p = self.x

        return (p**k)*(1-p)**(1-k)

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

