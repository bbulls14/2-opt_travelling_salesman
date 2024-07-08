from operator import itemgetter
from HashTable import HashTable
from WeightedGraph import Graph
from Logistics import Logistics
from Package import Package
from Truck import Truck

getAddresses: itemgetter = itemgetter(1)

logistics = Logistics()


truck1 = logistics.choosePackagesForTrucks()   
truckAddresses = truck1.packagesOnTruck

graph = Graph(truckAddresses)

graph.printMatrix()





# packagesassignedtotrucks = logistics.choosePackagesForTrucks()
# logistics.printKeyValuePairs(packagesassignedtotrucks)





# shortestDistances = graph.dijkstra(hashTable.find(1)) 

# graph.printGraph()
# hashTable.printKeyValuePairs()
