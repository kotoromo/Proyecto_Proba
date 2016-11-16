# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class Distribution:
    dist_type = ""

    __metaclass__ = ABCMeta

    @abstractmethod
    def getVar(self): pass

    @abstractmethod
    def getMed(self): pass

    @abstractmethod
    def getType(self): pass

    @abstractmethod
    def getDistribution(self): pass