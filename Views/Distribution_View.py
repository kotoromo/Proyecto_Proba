from abc import ABCMeta, abstractmethod


class DistributionView:
    __metaclass__= ABCMeta

    @abstractmethod
    def draw(self): pass

    @abstractmethod
    def clear(self): pass

    @abstractmethod
    def plot(self): pass

    @abstractmethod
    def maketop(self): pass