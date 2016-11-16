from Distribution import *
from Utilities.Maths import Maths

class Binomial(Distribution):
    type = "binomial"
    START = 1
    x = 0
    failure = 1-x
    x = 0
    n = 0

    def __init__(self, x, n, p):
        self.p = Maths.convertToDecimal(p)
        self.failure = 1-self.p
        self.x = int(x)
        self.n = int(n)

    def getProbability(self):
        n = self.n
        p = self.p
        k = self.x
        return float(Maths.Combination(n, k)*(p**k)*((1-p)**(n-k)))

    def getDistribution(self):
        pass

    def getMed(self):
        med = self.n*self.p

        return med

    def getType(self):
        return self.type

    def getVar(self):
        var = self.n*self.p*(1-self.p)
        return var

    def set_n(self, n):
        self.n = n

    def set_p(self, p):
        self.p = p

    def set_X(self, x):
        self.x = x
