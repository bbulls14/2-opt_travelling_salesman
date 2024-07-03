from HashTable import HashTable
from WeightedGraph import Graph, Vertex

hashTable = HashTable()

for packageID in range(1, 41):
    hashTable.insert(packageID)

print(hashTable)

