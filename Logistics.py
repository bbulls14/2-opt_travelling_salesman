from Package import Package
from operator import attrgetter, itemgetter

from Truck import Truck


class Logistics:
    def __init__(self, graph, hash_table):
        self.graph = graph
        self.hash_table = hash_table
        self.trucks = {}
        self.allPackages = Package.getPackageDataList() 
        
    
    # sourced from jamylak at https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value
    def sortPackagesForTrucks(self):
        distances = self.graph.dijkstra()
        sortedDistances = sorted(distances.items(), key=itemgetter(1))
        return sortedDistances
        
    def choosePackagesForTrucks(self):
        truck1 = Truck()
        # truck2 = Truck()
        # truck3 = Truck()
        getSpecialNote = attrgetter('specialNote')
        for package in self.allPackages:
            if '9:05' in getSpecialNote(package):
                self.trucks[truck1] = package
            # if 'Can only be on truck 2' in getSpecialNote(package):
            #     self.trucks[truck2] = package
        
        return self.trucks 
            

                
   