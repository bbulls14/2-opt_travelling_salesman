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
        # self.populateTable()

    
    def hash(self, key):
        return key - 1
    
    def insert (self, key): 
        if key < 1 or key > self.size:
            return "invalid packageID"      
        
        self.used += 1
        bucketID = self.hash(key)
        bd = self.hashPackageData[bucketID]
        bucketPackage = (bd.address, bd.deadline, bd.city, bd.zipCode, bd.weight, bd.status)
        bucket = self.hashMap[bucketID]
        
        if bucket is None:
            self.hashMap[bucketID] = Bucket(key, bucketPackage)
            return
        
        while bucket is not None:
            bucket = bucket.next
        bucket.next = Bucket(key, bucketPackage)
        
                
    def find(self, key):
        if key < 1 or key > self.size:
            return "invalid packageID"
                 
        
        bucketID = self.hash(key)
        bucket = self.hashMap[bucketID]
        
        while bucket is not None and bucket.key != key:
            bucket = bucket.next
            
        if bucket is None:
            return None
        else:
            return bucket.bucketPackage 
    
    def remove (self, key):
        if key < 1 or key > self.size:
            print("invalid packageID")
            return None      
        
        bucketID = self.hash(key)
        bucket = self.hashMap[bucketID]
        prev = None
        
        
        while bucket is not None and bucket.key != key:
            prev = bucket
            bucket = bucket.next
            
        if bucket is None:
            return None
        
        self.used -= 1
        result = bucket.key
        if prev is None:
            self.hashMap[bucketID] = bucket.next
        else:
            prev.next = bucket.next
        return result
        
    def __str__(self):
        output = []
        for buckets in self.hashMap:
            bucket = buckets
            while bucket is not None:
                output.append(str(bucket.bucketPackage))
                bucket = bucket.next
        return "\n".join(output)
    
    
    # def populateTable(self):
    #     key = (self.hashPackageData[0])
    #     for key in range(len(self.hashPackageData)):
    #         self.insert(key)
            
    def printKeyValuePairs(self):
        for bucket in self.hashMap:
            b = bucket
            while b is not None:
                b = b.next
        