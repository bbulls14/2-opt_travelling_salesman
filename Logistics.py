from datetime import datetime
from Package import Package
from operator import attrgetter, itemgetter

from Truck import Truck

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
        endOfBusiness = datetime.strptime('4:00 PM', '%I:%M %p')
        tenThirtyDeadline = datetime.strptime('10:30 AM', '%I:%M %p')
        nineAMDeadline = datetime.strptime('9:30 AM', '%I:%M %p')
        
        
        truck1Pkgs = []
        truck1Count = 0
        truck2Pkgs = []
        truck2Count = 0
        truck3Pkgs = []
        truck3Count = 0
    
        for package in self.allPackages:
            address = package.address
            deadline = package.deadline
            specialNote = package.specialNote

            if truck1Count<16 and nineAMDeadline == deadline:
                truck1Pkgs.append(package)
                truck1Count+=1
                
            elif truck2Count < 16 and (('Delayed on flight' in specialNote) or ('truck 2' in specialNote)
                                        or ('410 S State St' in address) or ('300 State St' in address) or
                                        [pkg for pkg in truck2Pkgs if pkg.address == address]):
                truck2Pkgs.append(package)
                truck2Count += 1    
                
            elif truck1Count < 16 and ((tenThirtyDeadline == deadline) or
                                    ('Must be delivered with' in specialNote) or 
                                    [pkg for pkg in truck1Pkgs if pkg.address == address]):
                truck1Pkgs.append(package)
                truck1Count += 1

            elif truck3Count < 16 and (endOfBusiness == deadline or
                                    [pkg for pkg in truck3Pkgs if pkg.address == address]):
                truck3Pkgs.append(package)
                truck3Count += 1


            else:
                if truck1Count < 16:
                    truck1Pkgs.append(package)
                    truck1Count += 1
                if truck2Count < 16:
                    truck2Pkgs.append(package)
                    truck2Count += 1
                if truck3Count < 16:
                    truck3Pkgs.append(package)
                    truck3Count += 1
                    
        return truck1Pkgs, truck2Pkgs, truck3Pkgs
                
 
    
 