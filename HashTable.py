from Package import Package

INITIAL_CAPACITY = 40

#referenced from PageKey at 6:19-10:17 of https://www.youtube.com/watch?v=zHi5v78W1f0&t=628s
class Bucket:
    def __init__(self, key, bucketPackage):
        self.key = key
        self.next = None
        self.bucketPackage = bucketPackage
    
    def __str__(self):
        if self.bucketPackage:
            return (self.bucketPackage)
        else:
            return "No package data"
        
class HashTable():
    def __init__(self):
        self.size = INITIAL_CAPACITY
        self.hashMap = [None] * self.size
        self.used = 0
        self.hashPackageData = Package.getPackageDataList()
        self.populateTable()

    #Direct mapping of packageID to key
    #first package is first index in hashTable
    def hash(self, key):
        return key - 1
    
    #self-adjusting function to resize hashMap and update with existing buckets
    def resize(self, newSize):
        oldHashMap = self.hashMap

        self.size = newSize
        self.hashMap = [None] * self.size

        for bucket in oldHashMap:
            if bucket is not None:
                self.rehash(bucket)
    #function to update resized hashMap with existing buckets
    def rehash(self, bucket):
        bucketID = self.hash(bucket.key)
        self.hashMap[bucketID] = bucket
    
    #insert using packageID
    #includes self-Adjusting function to resize if used buckets equals size of hashMap
    #try:catch to ensure that inserts for packageIDs are within range non-existant data     
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
            self.resize(newSize)
             
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
            return bucket.bucketPackage 
    
    # def remove (self, key):
    #     key = int(key)
        
    #     if key < 1 or key > self.size:
    #         return print(f"{key} is an invalid packageID")
                  
        
    #     bucketID = self.hash(key)
    #     bucket = self.hashMap[bucketID]
    #     prev = None
        
        
    #     while bucket is not None and bucket.key != key:
    #         prev = bucket
    #         bucket = bucket.next
            
    #     if bucket is None:
    #         return print(f"Package ID: {key} has no data")
        
    #     self.used -= 1
    #     result = bucket.key
    #     if prev is None:
    #         self.hashMap[bucketID] = bucket.next
    #     else:
    #         prev.next = bucket.next
    #     return result
        
    def __str__(self):
        output = []
        for buckets in self.hashMap:
            bucket = buckets
            while bucket is not None:
                output.append(str(bucket.bucketPackage))
                bucket = bucket.next
        return "\n".join(output)
    
    
    def populateTable(self):
        for package in self.hashPackageData:
            key = int(package.packageID)
            self.insert(key)
            
    def printKeyValuePairs(self):
        for bucket in self.hashMap:
            b = bucket
            while b is not None:
                b = b.next
        