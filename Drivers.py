import itertools
import Truck

class DriverCounter(object):
    counters = {}

    @classmethod
    def getCounter(cls, driver):
        cls.counters.setdefault(driver, itertools.count())
        return next(cls.counters[driver])
    
class Drivers():
    def __init__(self):
        self.driverID = DriverCounter.getCounter(self.__class__)
        self.truckID

