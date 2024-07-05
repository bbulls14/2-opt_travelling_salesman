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
        
    
    def getPackageDataList():
        packageData = []
        with open('WGUPS Packages.csv', mode = 'r', encoding='UTF-8-sig') as file:
            csvFile = csv.reader(file, delimiter=',')
            next(csvFile)
            for row in (csvFile):
                packageID = int(row[0])
                address = row[1]
                city = row[2]
                state = row[3]
                zipCode = row[4]
                deadline = row[5]
                weight = row[6]
                specialNote = row[7]
                status = "at the hub"
                
                package = Package(packageID, address, city, state, 
                                  zipCode, deadline, weight, specialNote, status)
                packageData.append(package)
        return packageData
    
    def __str__(self):
        return (f"PackageID: {self.packageID}, Address: {self.address}")
    
    
