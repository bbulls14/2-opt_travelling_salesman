import csv
from datetime import datetime

from Clock import Clock

class Package(object):
    def __init__(self, packageID, address, city, state, zipCode, 
                 deadline, weight, specialNote, status = "", ):
       

        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deadline = deadline
        self.weight = weight
        self.specialNote = specialNote
        self.status = ''
    
    def __str__(self):
        return (f"PackageID: {self.packageID}, Address: {self.address}, City: {self.city}, ZipCode: {self.zipCode} Deadline: {self.deadline}, Weight: {self.weight}, Status: {self.status}")
    
    def getPackageDataList():
        clock = Clock()
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
                    deadline = datetime.strptime('4:00 PM', '%I:%M %p')
                else:
                    deadline = datetime.strptime(deadline, '%I:%M %p')
                weight = row[6]
                specialNote = row[7]
                status = "at the hub"

                
                package = Package(packageID, address, city, state, 
                                  zipCode, deadline, weight, specialNote, status)
                packageData.append(package)
        return packageData
    
    def organizePackages(self):
        endOfBusiness = datetime.strptime('4:00 PM', '%I:%M %p')

        allPackages = self.getPackageDataList()
        
        truck1 = []
        truck2 = []
        truck3 = []
        
        index = 0
        while index < len(allPackages):
            package = allPackages[index]
            address = package.address
            deadline = package.deadline
            specialNote = package.specialNote
            pID = int(package.packageID)
            
            if 'wrong address' in specialNote:
                truck3.append(allPackages.pop(index))
                continue
            
            if 'truck 2' in specialNote or address in [p.address for p in truck2]:
                truck2.append(allPackages.pop(index))
                continue
                
            if 'Delayed on flight' in specialNote:
                truck2.append(allPackages.pop(index))
                continue

            if 'Must be delivered with' in specialNote or pID in {13, 15, 19} or address in [p.address for p in truck1]:
                truck1.append(allPackages.pop(index))
                continue
            
            if deadline < endOfBusiness:
                truck1.append(allPackages.pop(index))
                continue
            index += 1 

        index = 0
        while index < len(allPackages):
            if (len(truck3)<=16):
                truck3.append(allPackages.pop(index))
                continue
            
            if (len(truck2)<=16):
                truck2.append(allPackages.pop(index))
                continue
            
            if (len(truck1)<-16):
                truck1.append(allPackages.pop(index))
                continue
            index+=1
                        
        return truck1, truck2, truck3
