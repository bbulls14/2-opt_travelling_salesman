from operator import itemgetter
from LocalAdjMatrix import Matrix
from Logistics import Logistics
from TwoOptAlgorithm import TwoOptAlgorithm

# emptyMatrix = Matrix()
# getAddresses: itemgetter = itemgetter(1)

# logistics = Logistics()

# truck1, truck2, truck3 = logistics.choosePackagesForTrucks() 
# emptyMatrix.twoOptAlgo(truck1)
logistics = Logistics()
truck1, truck2, truck3 = logistics.choosePackagesForTrucks()
matrix1 = Matrix()
matrix2 = Matrix()
matrix3 = Matrix()

algorithm1 = TwoOptAlgorithm(matrix1)
algorithm2 = TwoOptAlgorithm(matrix2)
algorithm3 = TwoOptAlgorithm(matrix3)


edges1, indices1, originalList1 = matrix1.localMatrix(truck1)
edges2, indices2, originalList2 = matrix2.localMatrix(truck2)
edges3, indices3, originalList3 = matrix3.localMatrix(truck3)

addressPath1, distances1 = algorithm1.bestPath()
addressPath2, distances2 = algorithm2.bestPath()
addressPath3, distances3 = algorithm3.bestPath()

print(f"final address path: {addressPath1}")
print(f"distances for each edge: {distances1}")

print(f"final address path: {addressPath2}")
print(f"distances for each edge: {distances2}")  

print(f"final address path: {addressPath3}")
print(f"distances for each edge: {distances3}")  


# truck2Address, truck2Distance = Matrix(truck2)
# print(f"final address path: {truck2Address}")
# print(f"distances for each edge: {truck2Distance}")
# truck3Address, truck3Distance = Matrix(truck3)
# print(f"final address path: {truck3Address}")
# print(f"distances for each edge: {truck3Distance}")






# packagesassignedtotrucks = logistics.choosePackagesForTrucks()
# logistics.printKeyValuePairs(packagesassignedtotrucks)





# shortestDistances = graph.dijkstra(hashTable.find(1)) 

# graph.printGraph()
# hashTable.printKeyValuePairs()
