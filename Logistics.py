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
        truck1 = Truck()
        # truck2 = Truck()
        # truck3 = Truck()
        getID = attrgetter('packageID')
        getDeadline = attrgetter('deadline')
        getAddress = attrgetter('address')
        for package in self.allPackages:
            # if endOfBusiness != getDeadline(package):
            #     truck1.packagesOnTruck.append(getAddress(package))
            if '1060' in getAddress(package):
                truck1.packagesOnTruck.append(getAddress(package))
            elif '1330 2100' in getAddress(package):
                truck1.packagesOnTruck.append(getAddress(package))
            elif '1488 4800' in getAddress(package):
                truck1.packagesOnTruck.append(getAddress(package))
            elif '177 W' in getAddress(package):
                truck1.packagesOnTruck.append(getAddress(package))
            elif '195 W' in getAddress(package):
                truck1.packagesOnTruck.append(getAddress(package))
            # if '9:05' in getSpecialNote(package):
            #     self.trucks[truck1] = package
            # if 'Can only be on truck 2' in getSpecialNote(package):
            #     self.trucks[truck2] = package
        
        return truck1 
            
            
   