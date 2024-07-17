import itertools
from datetime import datetime
from Clock import Clock


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
        self.route = []
        self.orderedDistances = []
        

    
    def __str__(self) -> str:
        return (f"truckId: {self.truckID}, NumberofPackages: {self.numPackages}, Departure Time: {self.departureTime}")
    
#update status of ONE package
def updateStatus(timeObj, pid, truck):
    clock = Clock()
    
    if timeObj < truck.departureTime:
        for pkg in truck.packagesOnTruck:
            if pid == pkg.packageID:
                pkg.status = "at the hub"
                return

    while clock.getTime() < timeObj:
        for i in range(len(truck.orderedDistances)):
            distance = truck.orderedDistances[i]
            timePassed = (distance / 18) * 60
            clock.addMinutes(timePassed)
            
            for pkg in truck.packagesOnTruck:
                pkgAddress = pkg.address
                if pid == pkg.packageID:
                    if truck.route[i + 1] == pkgAddress:
                        if clock.getTime() < pkg.deadline:
                            pkg.status = "delivered at " + str(clock.getTime())
                            return
                        else:
                            pkg.status = "delivered late at " + str(clock.getTime())
                            return

    # If the loop completes and the package is still undelivered
    for pkg in truck.packagesOnTruck:
        if pid == pkg.packageID:
            if clock.getTime() < timeObj:
                pkg.status = "en route" 