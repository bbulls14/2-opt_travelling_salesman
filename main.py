from datetime import datetime
from HashTable import HashTable
from AdjMatrix import Matrix
from Package import organizePackages
from Truck import Truck, updateStatus

endOfBusiness = datetime.strptime('4:00 PM', '%I:%M %p')
startOfBusiness = datetime.strptime('8:00 AM', '%I:%M %p')


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

truck1.orderedDistances = distances1
truck2.orderedDistances = distances2
truck3.orderedDistances = distances3


print('*******************************************************************************\n')

print('Welcome to the WGUPS Delivery Interface\n')

while True:
    try:
        time = input("What time is it? __:__ AM/PM\n")
        timeObj = datetime.strptime(time, "%I:%M %p")
        break              
    except:
        print("\nInvalid Input, use the correct format for hour and minute.\nDon't forget the ':' and include AM or PM at the end\n")
# if startOfBusiness > timeObj > endOfBusiness 

print('\n1. Look up a Package')
print('2. View All Packages\n')

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
            pid = input('What is the packageID that you would like to check?\n')
            0 < int(pid) <= hash.used
            break
        except:
            print('Please enter a valid packageID\n')
    
    for pkg in truck1.packagesOnTruck:
        if pkg.packageID == pid:
            updateStatus(timeObj, pid, truck1)
    for pkg in truck2.packagesOnTruck:
        if pkg.packageID == pid:
            updateStatus(timeObj, pid, truck2)    
    for pkg in truck3.packagesOnTruck:
        if pkg.packageID == pid:
            updateStatus(timeObj, pid, truck3)  

# if num == '2':
    
    # updateTruckDistance(truckOrAll, timeObj)
        












