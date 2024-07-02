import HashTable
import Package

hashTable = HashTable.HashTable()

for packageID in range(1, 41):
    hashTable.insert(packageID)
    
print(hashTable.find(1))