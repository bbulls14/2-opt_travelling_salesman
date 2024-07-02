# import pandas lib as pd
import pandas as pd
from Package import Package

INITIAL_CAPACITY = 40
class Node:
    def __init__(self, key):
        self.key = key
        self.hashPackage = self.getHashMapPackageData(key)
        self.next = None
    
    def getHashMapPackageData(self, key): 
        data = pd.read_excel('WGUPS Package File.xlsx')
        row = key+6
        packageID = data.iloc[row,0]
        address = data.iloc[row,1]
        city = data.iloc[row,2]
        zipCode = data.iloc[row,4]
        deadline = data.iloc[row,5]
        weight = data.iloc[row,6]
        status = "at the hub"
        return Package.forHashMap(packageID, address, city, zipCode, deadline, weight, status)
 
        
class HashTable():
    def __init__(self):
        self.size = INITIAL_CAPACITY
        self.buckets = [None] * self.size
        self.used = 0
        
    def hash(self, key):
        return key -1
    
    def insert (self, key):
        self.used += 1
        index = self.hash(key)
        node = self.buckets[index]
        
        if node is None:
            self.buckets[index] = Node(key)
            return
        prev = node
        
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key)
        
                
    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        
        while node is not None and node.key != key:
            node = node.next
            
        if node is None:
            return None
        else:
            return node
    
    
    def remove (self, key):
        index = self.hash(key)
        node = self.buckets[index]
        
        while node is not None and node.key != key:
            prev = node
            node = node.next
            
        if node is None:
            return None
        else:
            self.used -= 1
            result = node
            if prev is None:
                node = None
            else:
                prev.next = node.next
                return result
            
  
  
  
# if __name__ == "__main__":      

#     hashTable = HashTable()
    
#     for row in range (7, 47):

#         packageTraits = []
#         for col in range (0, 7):
#             packageTraits.append(packagesExcel.iat[row, col])
                 

#         package = Package.HashPackage(
#             packageID = packageTraits[0],
#             address = packageTraits[1],
#             city = packageTraits[2],
#             zipCode = packageTraits [3],
#             deadline = packageTraits[5],
#             weight = packageTraits[6],
#             # specialNotes = packageTraits[7],
#             status = "at the hub"
#         )
#         hashTable.insert(package)
        

# for index, bucket in enumerate(hashTable.table):
#     if bucket:
#         print(f"Index {index + 1}: {bucket}")






