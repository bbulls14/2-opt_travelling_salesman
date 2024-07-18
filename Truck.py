import itertools
from datetime import datetime


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
        self.packagesOnTruck = []
        self.milesDriven = 0
        if self.truckID == 0:
            self.departureTime = datetime.strptime('8:00 AM', '%I:%M %p')
        if self.truckID == 1:
            self.departureTime = datetime.strptime('9:05 AM', '%I:%M %p')
        if self.truckID == 2:
            self.departureTime = datetime.strptime('10:20 AM', '%I:%M %p')
        self.route = []
        self.orderedDistances = []

    
    def __str__(self) -> str:
        return (f"truckId: {self.truckID}, Departure Time: {self.departureTime.strftime('%I:%M %p')}, Miles Driven: {"%.2f" % self.milesDriven}")
    
 #flow: called at start of updatePkgsStatus in main.py  
 #process: 
 # 1. initialize empty list 
 # 2. iterate through truck.route -> iterate through truck.packagesOnTruck and check if address matches truck.route address 
 # 3. update orderedPkgs list if it does, otherwise, continue
    def orderPackagesByRoute(self):
        orderedPkgs = []
        for route in self.route:
            if route == 'HUB':#skip because no package has this address
                continue
            for pkg in self.packagesOnTruck:
                if route == pkg.address:
                    orderedPkgs.append(pkg)
        return orderedPkgs

