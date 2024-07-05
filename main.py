from HashTable import HashTable
from WeightedGraph import Graph
from Logistics import Logistics
from Package import Package

hashTable = HashTable()
graph = Graph()
logistics = Logistics(graph, hashTable)

best_packages = logistics.sortPackagesForTrucks()

print("Best packages to load onto the truck:")
for package in best_packages:
    print(package)



# shortestDistances = graph.dijkstra(hashTable.find(1)) 

# graph.printGraph()
# hashTable.printKeyValuePairs()
