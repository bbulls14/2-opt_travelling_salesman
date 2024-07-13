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
    def __init__(self, packagesOnTruck):
        self.truckID = TruckCounter.getCounter(self.__class__)+1
        self.packagesOnTruck = packagesOnTruck
        self.numPackages = len(packagesOnTruck)
        self.milesDriven = 0
        if self.truckID == 1:
            self.departureTime = '8:00 AM'
        if self.truckID == 2:
            self.departureTime = '9:05 AM'
        if self.truckID == 3:
            self.departureTime = '10:20 AM'
        

    
    def __str__(self) -> str:
        return (f"truckId: {self.truckID}, NumberofPackages: {self.numPackages}, Departure Time: {self.departureTime}")
    
    
    # load truck1 manually with 1030pkgs, set departure time to 8am, load truck2 with truck 2 and delayed pkgs, set departure time to 905, load truck 3 with wrong address and any remaining pkgs set departure time to 1020
    
    # build matrix from listOfpkgs, find bestpath, add time penalty, when path is created test to see if route delivers all packages by required deadline, if true, approve rout
    
    
    # Interface:
    #     input time, use this to adjust pkgs status, 
    #     If pkg on truck that left depot
    #         change status to enRoute or delivered, based on time
    #     If pkg on truck that is at depot, change status to at hub and time
        