from Package import Package
import csv

INITIAL_CAPACITY = 40
class Node:
    def __init__(self, key, hashMapPackageData):
        self.key = key
        self.hashPackage = hashMapPackageData
        self.next = None
    
    def __str__(self):
        if self.hashPackage:
            return str(self.hashPackage)
        else:
            return "No package data"
        
class HashTable():
    def __init__(self):
        self.size = INITIAL_CAPACITY
        self.buckets = [None] * self.size
        self.used = 0
        self.hashMapPackageData = self.getHashMapPackageData('WGUPS Packages.csv')
        
    def getHashMapPackageData(self, filePath): 
        hashMapPackageData = {}
        with open(filePath, mode = 'r', encoding='UTF-8-sig') as file:
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
                hashMapPackageData[packageID] = Package.forHashMap(packageID, address, city, zipCode, deadline, weight, status)
        return hashMapPackageData    
        
    def hash(self, key):
        return key - 1
    
    def insert (self, key):
        self.used += 1
        index = self.hash(key)
        hashMapPackageData = self.hashMapPackageData.get(key, None)
        node = self.buckets[index]
        
        if node is None:
            self.buckets[index] = Node(key, hashMapPackageData)
            return
        
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, hashMapPackageData)
        
                
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
            
  