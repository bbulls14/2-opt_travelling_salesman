from operator import itemgetter
from HashTable import HashTable
from LocalAdjMatrix import Matrix
from Logistics import Logistics
from Package import Package
from Truck import Truck

getAddresses: itemgetter = itemgetter(1)

logistics = Logistics()


truck1 = logistics.choosePackagesForTrucks()   
truckAddresses = truck1.packagesOnTruck
matrix = Matrix(truckAddresses)
addressPath, distances = matrix.twoOptAlgo()

print(f"final address path: {addressPath}")
print(f"distances for each edge: {distances}")




# packagesassignedtotrucks = logistics.choosePackagesForTrucks()
# logistics.printKeyValuePairs(packagesassignedtotrucks)





# shortestDistances = graph.dijkstra(hashTable.find(1)) 

# graph.printGraph()
# hashTable.printKeyValuePairs()
