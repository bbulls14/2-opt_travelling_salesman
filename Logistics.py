from datetime import datetime
from Package import Package
from operator import attrgetter, itemgetter

from Truck import Truck
endOfBusiness = datetime.strptime('4:00 PM', '%H:%M %p').time()

class Logistics:
    def __init__(self):
        # self.graph = graph
        # self.hash_table = hash_table
        self.trucks = {}
        self.allPackages = Package.getPackageDataList() 
        
    
    # Lines 15-18 sourced from jamylak at https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value
    # def sortPackagesForTrucks(self, listOfVertices):
    #     distances = self.graph.dijkstra(listOfVertices)
    #     sortedDistances = sorted(distances, key=itemgetter(0,1))
        
    #     return sortedDistances
        
    def choosePackagesForTrucks(self):
        endOfBusiness = datetime.strptime('4:00 PM', '%I:%M %p').time()
        tenThirtyDeadline = datetime.strptime('10:30 AM', '%I:%M %p').time()  # Changed 'PM' to 'AM'
    
        truck1Pkgs = []
        truck1Count = 0
        truck2Pkgs = []
        truck2Count = 0
        truck3Pkgs = []
        truck3Count = 0
    
        getDeadline = attrgetter('deadline')
        getSpecialNote = attrgetter('specialNote')
        getAddress = attrgetter('address')
    
        for package in self.allPackages:
            if truck1Count < 16 and ((tenThirtyDeadline == getDeadline(package) and 'Delayed on flight' not in getSpecialNote(package)) or
                                    ('Must be delivered with' in getSpecialNote(package)) or
                                    getAddress(package) not in truck1Pkgs):
                truck1Pkgs.append(getAddress(package))
                truck1Count += 1
            elif truck2Count < 16 and ((tenThirtyDeadline == getDeadline(package) and 'Delayed on flight' in getSpecialNote(package)) or
                                        ('truck 2' in getSpecialNote(package)) or
                                        getAddress(package) not in truck2Pkgs):
                truck2Pkgs.append(getAddress(package))
                truck2Count += 1
            elif truck3Count < 16 and (endOfBusiness == getDeadline(package) or
                                        getAddress(package) not in truck3Pkgs):
                truck3Pkgs.append(getAddress(package))
                truck3Count += 1
    
        return truck1Pkgs, truck2Pkgs, truck3Pkgs
                
 
    
 