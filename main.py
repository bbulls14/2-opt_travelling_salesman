from operator import itemgetter
from LocalAdjMatrix import Matrix
from Logistics import Logistics

emptyMatrix = Matrix()
getAddresses: itemgetter = itemgetter(1)

logistics = Logistics()


truck1, truck2, truck3 = logistics.choosePackagesForTrucks() 
emptyMatrix.twoOptAlgo(truck1)


print(f"final address path: {truck1Address}")
print(f"distances for each edge: {truck1Distance}")
truck2Address, truck2Distance = Matrix(truck2)
print(f"final address path: {truck2Address}")
print(f"distances for each edge: {truck2Distance}")
truck3Address, truck3Distance = Matrix(truck3)
print(f"final address path: {truck3Address}")
print(f"distances for each edge: {truck3Distance}")






# packagesassignedtotrucks = logistics.choosePackagesForTrucks()
# logistics.printKeyValuePairs(packagesassignedtotrucks)





# shortestDistances = graph.dijkstra(hashTable.find(1)) 

# graph.printGraph()
# hashTable.printKeyValuePairs()
