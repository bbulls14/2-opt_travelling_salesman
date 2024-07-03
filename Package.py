import csv

class Package(object):
    def __init__(self, packageID=None, address=None, city=None, state=None, zipCode=None, 
                 deadline=None, weight=None, specialNote=None, status = ""):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deadline = deadline
        self.weight = weight
        self.specialNote = specialNote
        self.status = status
    
    @classmethod
    def forHashMap(cls, packageID, address, city, zipCode, deadline, weight, status):
        return cls(packageID=packageID, address=address, deadline=deadline, city=city, 
                   zipCode=zipCode, weight=weight, status=status)
        
    def __str__(self):
        return (f"PackageID: {self.packageID}, Address: {self.address}")
    
