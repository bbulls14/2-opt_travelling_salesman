from datetime import datetime
from Package import getPackageDataList
INITIAL_CAPACITY = 40

###lines 5-11 (PageKey, 2017)
class Bucket:
    def __init__(self, key, bucketPackage):
        self.key = key #packageID
        self.next = None
        #tuple(address, deadline, city, zipCode, weight, status)
        self.bucketPackage = bucketPackage
    
    def __str__(self):
        if self.bucketPackage:
            bp = self.bucketPackage
            deadlineStr = datetime.strftime(bp[1], "%I:%M %p")
            return (f"PackageID: {self.key}, Address: {bp[0]}, Deadline: {deadlineStr}, Status: {bp[5]} ")
        else:
            return "No package data"
### lines 21-25 (PageKey, 2017)        
class HashTable():
    def __init__(self):
        self.size = INITIAL_CAPACITY
        self.hashMap = [None] * self.size
        self.used = 0
        self.hashPackageData = getPackageDataList()
        self.populateTable()

    #Direct mapping of packageID to key
    #first package is first index in hashTable
    #Time/Space Complexity: O(1)
    def hash(self, key):
        return key - 1
    
    #self-adjusting function to resize hashMap and update with existing buckets
    #Time/Space complexity is O(2n) because hashmap doubles in size
    def resize(self, newSize):
        oldHashMap = self.hashMap

        self.size = newSize
        self.hashMap = [None] * self.size #Time/Space Complexity: O(2n)

        for bucket in oldHashMap: #Time/Space complexity O(n)
            if bucket is not None:
                self.rehash(bucket)
                
    #update resized hashMap with existing buckets
    def rehash(self, bucket):
        bucketID = self.hash(bucket.key)
        self.hashMap[bucketID] = bucket
    
    #insert using packageID
    #includes self-Adjusting function to resize if used buckets equals size of hashMap
    #try->catch to ensure that inserts for packageIDs are within range and exclude non-existant data
    #Time/Space Complexity: O(2n)    
    #       a. Time complexity depends on whether resize() is called, 
    #               when it's called the Time/Space Complexity is O(2n) because the hashMap doubles in size
    #       b. when resize is not called, the Time Complexity is O(n) because of collision management 
    #               and Space Complexity is O(1)
### 61-93 (PageKey, 2017)   
    def insert (self,key):
        key = int(key)
             
        if key < 1:
            return print(f"{key} is an invalid packageID")      

        #catch Index out of Range
        bucketID = self.hash(key)
        try:
            bd = self.hashPackageData[bucketID]
            bucketPackage = (bd.address, bd.deadline, bd.city, bd.zipCode, bd.weight, bd.status)
        except IndexError:
            return print(f"IndexError: packageID {key} is not within package data range")
        
        self.used+=1
        #self adjusts to double size if approaching capacity
        if self.used >= self.size:
            newSize = self.size * 2 
            self.resize(newSize) #Time/SpaceComplexity: O(2n)
             
        bucket = self.hashMap[bucketID]
        
        if bucket is None:
            self.hashMap[bucketID] = Bucket(key, bucketPackage)
            return
        
        #handles collision by setting bucket to None and then reupdateing with existing data
        #removes counter to maintain accurate used variable
        while bucket is not None:
            bucket = bucket.next     
        bucket = Bucket(key, bucketPackage)
        self.used-=1
        return print(f"Collision: repopulated packageID {key} with existing data")

    #update bucket in hashTable values from a pkg
    #Time complexity: O(n) because of collision management, Space Complexity: O(1) because bucketPackage is a fixed length of 6
    def update(self, key, pkg):
        key = int(key)
        if key < 1 or key > self.used:
            return print(f"{key} is an invalid packageID")
        
        bucketID = self.hash(key)
        bucket = self.hashMap[bucketID]
        
        #handle collision by traversing through list if the bucket key doesnt equal the input key
        while bucket is not None and bucket.key != key:
            bucket = bucket.next
        
        if bucket is None:
            return print(f"Package ID: {key} has no data")
        else:    
            bucketPackageList = list(bucket.bucketPackage)
            
            bucketPackageList[0] = pkg.address
            bucketPackageList[1] = pkg.deadline
            bucketPackageList[2] = pkg.city
            bucketPackageList[3] = pkg.zipCode
            bucketPackageList[4] = pkg.weight
            bucketPackageList[5] = pkg.status
            
            updatedBucket = tuple(bucketPackageList)
            self.hashMap[bucketID] = Bucket(key, updatedBucket)

    #look-up bucket using packageID    
    #Time complexity: O(n) because of collision management, Space Complexity: O(1) because bucketPackage is a fixed length of 6            
### lines 127-143 (PageKey, 2017)    
    def find(self, key):
        key = int(key)
        if key < 1 or key > self.size:
            return print(f"{key} is an invalid packageID")
                 
        
        bucketID = self.hash(key)
        bucket = self.hashMap[bucketID]
        
        #handle collision by traversing through list if the bucket key doesnt equal the input key
        while bucket is not None and bucket.key != key:
            bucket = bucket.next
            
        if bucket is None:
            return print(f"Package ID: {key} has no data")
        else:
            return str(bucket) 
        
    def __str__(self):
        output = []
        for buckets in self.hashMap:
            bucket = buckets
            while bucket is not None:
                output.append(str(bucket.bucketPackage))
                bucket = bucket.next
        return "\n".join(output)
    
    #iterate through packages from getPackageData in Package.py, call insert() for each packageID
    #insert package using packageID as key
    #Time/Space Complexity: O(2n^2)
    #       a. when resize() is not called in insert() function
    #           i. Time/Space Complexity: O(n^2) 
    def populateTable(self):
        for package in self.hashPackageData: #Time/Space Complexity O(n)
            key = int(package.packageID)
            self.insert(key) #Time/Space Complexity: O(2n)


                                         