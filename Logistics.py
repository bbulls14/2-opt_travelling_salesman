from Package import Package
from operator import itemgetter


class Logistics:
    def __init__(self, graph, hash_table):
        self.graph = graph
        self.hash_table = hash_table
        self.trucks = []
        self.allPackages = Package.getPackageDataList() 
        
    # def determine_best_packages(self, num_packages=17):
    #     distances = self.graph.dijkstra()
    #     sorted_packages = sorted(distances.items(), key=lambda item: item[1])[:num_packages]
    #     return [package[0] for package in sorted_packages]
    
    # sourced from jamylak at https://stackoverflow.com/questions/10695139/sort-a-list-of-tuples-by-2nd-item-integer-value
    def sortPackagesForTrucks(self):
        distances = self.graph.dijkstra()
        sortedDistances = sorted(distances, key=itemgetter(1))
        return sortedDistances
        
        