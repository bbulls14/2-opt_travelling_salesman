from Package import Package
import csv

INITIAL_CAPACITY = 40



class Node:
    def __init__(self, key, hashMapPackage):
        self.key = key
        self.hashPackage = hashMapPackage
        self.next = None
    
    def __str__(self):
        if self.hashPackage:
            return str(Package(self.hashPackage))
        else:
            return "No package data"
        
class HashTable():
    def __init__(self):
        self.size = INITIAL_CAPACITY
        self.buckets = [None] * self.size
        self.used = 0
        self.hashMapPackageData = self.getHashMapPackageData()
        self.populateTable()
           
    def getHashMapPackageData(self): 
        hashMapPackageData = []
        with open('WGUPS Packages.csv', mode = 'r', encoding='UTF-8-sig') as file:
            csvFile = csv.reader(file, delimiter=',')
            next(csvFile)
            for row in csvFile:
                packageID = int(row[0])
                address = row[1]
                city = row[2]
                zipCode = row[5]
                deadline = row[6]
                weight = row[7]
                status = "at the hub"
            
                package = Package.forHashMap(packageID, address, city, zipCode, deadline, weight, status)
                hashMapPackageData.append((packageID, package))
        return hashMapPackageData
    
    def hash(self, key):
        return key - 1
    
    def insert (self, key):
        self.used += 1
        index = self.hash(key)
        hashPackage = self.hashMapPackageData[index][1]
        node = self.buckets[index]
        
        if node is None:
            self.buckets[index] = Node(key, hashPackage)
            return
        
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, hashPackage)
        
                
    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        
        while node is not None and node.key != key:
            node = node.next
            
        if node is None:
            return None
        else:
            return node.hashPackage.address 
    
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
            result = node.hashPackage
            if prev is None:
                self.buckets[index] = node.next
            else:
                prev.next = node.next
            return result
        
    def __str__(self):
        output = []
        for bucket in self.buckets:
            node = bucket
            while node is not None:
                output.append(str(node))
                node = node.next
        return "\n".join(output)
    
    def populateTable(self):
        for i in range(0, len(self.hashMapPackageData)):
            self.insert(self.hashMapPackageData[i][0])
            
    def printKeyValuePairs(self):
        for bucket in self.buckets:
            node = bucket
            while node is not None:
                print(f"Key: {node.key}, Value: {node.hashPackage}")
                node = node.next
                
        