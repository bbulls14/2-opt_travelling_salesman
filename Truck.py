import itertools
from datetime import datetime
from Package import Package
from HashTable import HashTable

# Incrementing ID (lines 6-12, 16) from selcuk at https://stackoverflow.com/questions/71520394/create-an-incremental-id-in-a-python-class-with-subclasses-each-maintaining-thei
class TruckCounter(object):
    counters = {}

    @classmethod
    def getCounter(cls, truck):
        cls.counters.setdefault(truck, itertools.count())
        return next(cls.counters[truck])
    
class Truck():
    def __init__(self):
        self.truckID = TruckCounter.getCounter(self.__class__)
        self.numPackages = 0
        self.packagesOnTruck = []
        self.milesDriven = 0
        self.departureTime = datetime.time(8,00,00)

    
    def __str__(self) -> str:
        return (f"truckId: {self.truckID}, NumberofPackages: {self.numPackages}, Departure Time: {self.departureTime}")
    # def loadTruck():
        