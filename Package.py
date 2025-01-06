import csv
from datetime import datetime


class Package(object):
    def __init__(self, packageID, address, city, state, zipCode, 
                 deadline, weight, specialNote, status):

        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deadline = deadline
        self.weight = weight
        self.specialNote = specialNote
        self.status = status

    
    def __str__(self):
        return (f"PackageID: {self.packageID}, Address: {self.address}, City: {self.city}, ZipCode: {self.zipCode} Deadline: {self.deadline}, Weight: {self.weight}, Status: {self.status}")

#flow: accessed by HashTable.py and organizePackages() in Packages.py
#process: 
# 1. create empty list PackageData
# 2. accesses data in Packages csv file
# 3. obtains attributes of package by iterating through rows 
# 4. creates package objects for each iteration 
# 5. appends PackageData with package object
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
            if 'EOD' in deadline: #create datetime object for deadline
                deadline = datetime.strptime('4:00 PM', '%I:%M %p')
            else:
                deadline = datetime.strptime(deadline, '%I:%M %p')
            weight = row[6]
            specialNote = row[7]
            status = '' #empty string to update with 'at the hub'/'delivered'/'en route' + time

            
            package = Package(packageID, address, city, state, 
                                zipCode, deadline, weight, specialNote, status)
            packageData.append(package)
    return packageData

#flow: called from main.py after timeObj input -> load packages onto trucks based on paramaters
#process: 
# 1. create list allPackages using getPackageData 
# 2. Iterate through list, pop pkg out, sort into truck.packagesOnTruck based on pkg attributes or if address matches another address in list
# 3. packages without special considerations are sorted onto trucks as long as the number of packages on the truck is less than 16

def organizePackages(hash, timeObj, truck1, truck2, truck3):
    endOfBusiness = datetime.strptime('4:00 PM', '%I:%M %p')

    allPackages = getPackageDataList() #Time/Space Complexity: O(n)

    
    index = 0
    while index < len(allPackages):
        pkg = allPackages[index]
        address = pkg.address
        deadline = pkg.deadline
        specialNote = pkg.specialNote
        pID = int(pkg.packageID)
        
        if 'Wrong address' in specialNote:
            if timeObj < truck3.departureTime:
                pkg = allPackages.pop(index) #Time Complexity for EACH pop(): O(n)
                truck3.packagesOnTruck.append(pkg) 
            else:
                pkg = allPackages.pop(index)
                pkg.address = '410 S State St'
                pkg.zipCode = '84111'
                pkg.specialNote = 'Address corrected'
                truck3.packagesOnTruck.append(pkg) 
                hash.update(pkg.packageID, pkg) 
            continue
        
        if 'truck 2' in specialNote or address in [p.address for p in truck2.packagesOnTruck]: 
            pkg = allPackages.pop(index)
            truck2.packagesOnTruck.append(pkg)
            continue
            
        if 'Delayed on flight' in specialNote:
            pkg = allPackages.pop(index)
            if timeObj < truck2.departureTime:
                truck2.packagesOnTruck.append(pkg)
            else:
                pkg.specialNote = "Received from Flight"
                truck2.packagesOnTruck.append(pkg)
                hash.update(pkg.packageID, pkg)
            continue

        if 'Must be delivered with' in specialNote or pID in {13, 15, 19} or address in [p.address for p in truck1.packagesOnTruck]:
            pkg = allPackages.pop(index)
            truck1.packagesOnTruck.append(pkg)
            continue
        
        if deadline < endOfBusiness:
            pkg = allPackages.pop(index)
            truck1.packagesOnTruck.append(pkg)
            continue
        index += 1 

    index = 0
    while index < len(allPackages):
        pkg = allPackages[index]
        if (len(truck3.packagesOnTruck)<=16):
            pkg = allPackages.pop(index)
            truck3.packagesOnTruck.append(pkg)
            continue
        
        if (len(truck3.packagesOnTruck)<=16):
            pkg = allPackages.pop(index)
            truck2.packagesOnTruck.append(pkg)
            continue
        
        if (len(truck3.packagesOnTruck)<-16):
            pkg = allPackages.pop(index)
            truck1.packagesOnTruck.append(pkg)
            continue
        index+=1
         
              

