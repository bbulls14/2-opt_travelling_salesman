import csv
from datetime import datetime

startTime = datetime.strptime(f'8:00 AM', '%H:%M %p').time()

class Package(object):
    

    def __init__(self, packageID, address, city, state, zipCode, 
                 deadline, weight, specialNote, status = ""):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deadline = deadline
        self.weight = weight
        self.specialNote = specialNote
        self.status = f"{status} {startTime}"
    
    def __str__(self):
        return (f"PackageID: {self.packageID}, Address: {self.address}, City: {self.city}, ZipCode: {self.zipCode} Deadline: {self.deadline}, Weight: {self.weight}, Status: {self.status}")
    
    def getPackageDataList():
        packageData = []
        with open('WGUPS Packages.csv', mode = 'r', encoding='UTF-8-sig') as file:
            csvFile = csv.reader(file, delimiter=',')
            next(csvFile)
            for row in (csvFile):
                packageID = row[0]
                address = row[1]
                city = row[2]
                state = row[3]
                zipCode = row[4]
                deadline = row[5]
                if 'EOD' in deadline:
                    deadline = datetime.strptime('4:00 PM', '%H:%M %p').time()
                else:
                    deadline = datetime.strptime(deadline, '%H:%M %p').time()
                weight = row[6]
                specialNote = row[7]
                status = "at the hub"
                
                package = Package(packageID, address, city, state, 
                                  zipCode, deadline, weight, specialNote, status)
                packageData.append(package)
        return packageData
    
    # def updateStatus():
