from datetime import datetime
from HashTable import HashTable
from AdjMatrix import Matrix
from Package import organizePackages
from Truck import Truck

hash = HashTable()

matrix1 = Matrix()
matrix2 = Matrix()
matrix3 = Matrix()

truck1Pkgs, truck2Pkgs, truck3Pkgs = organizePackages()

truck1 = Truck(truck1Pkgs)
truck2 = Truck(truck2Pkgs)
truck3 = Truck(truck3Pkgs)

matrix1 = matrix1.matrixAttributes(truck1.packagesOnTruck)
matrix2 = matrix2.matrixAttributes(truck2.packagesOnTruck)
matrix3 = matrix3.matrixAttributes(truck3.packagesOnTruck)



tour1, distances1 = matrix1.bestPath(truck1)
tour2, distances2 = matrix2.bestPath(truck2)
tour3, distances3 = matrix3.bestPath(truck3)


print('*******************************************************************************\n')

print('Welcome to the WGUPS Delivery Interface\n')

while True:
    try:
        time = input("What time is it? __:__ AM/PM\n")
        timeObj = datetime.strptime(time, "%I:%M %p")
        break
    except:
        print("\nInvalid Input, use the correct format for hour and minute.\nDon't forget the ':' and include AM or PM at the end\n")

print('\n1. Check the status of a package')
print('2. Check miles traveled by a truck\n')

while True:
    num = input('What would you like to do? Type 1 or 2\n')
    try:
        int(num) == 1 or int(num) == 2
        break
    except:
        print('Please input either 1 or 2')

if num == '1':
    while True:
        print('\nChecking the status of a package.....')
        try:
            pid = int(input('What is the packageID that you would like to check?\n'))
            0 < pid <= hash.used
            break
        except:
            print('Please enter a valid packageID\n')
    pkgToCheck = hash.find(pid)
    for pkg in truck1.packagesOnTruck:
        if pkg.packageID == pid:
            hash.updatePkgStatus(timeObj, pkgToCheck, truck1)
    for pkg in truck2.packagesOnTruck:
        if pkg.packageID == pid:
            hash.updatePkgStatus(timeObj, pkgToCheck, truck2)    
    for pkg in truck3.packagesOnTruck:
        if pkg.packageID == pid:
            hash.updatePkgStatus(timeObj, pkgToCheck, truck3)  

if num == '2':
    while True:
        truckOrAll = input("Enter the truckID (1, 2, or 3) if you want to check a specific truck.\nEnter all if you want to check the total distance traveled\n")
        try:
            truckOrAll == '1' or truckOrAll == '2' or truckOrAll == '3' or truckOrAll.lower() == 'all'
            break
        except:
            print('Please enter 1, 2, 3, or all.') 
    # updateTruckDistance(truckOrAll, timeObj)
        












