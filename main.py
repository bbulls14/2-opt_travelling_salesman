from datetime import datetime, timedelta
from HashTable import HashTable
from AdjMatrix import Matrix
from Package import organizePackages
from Truck import Truck

endOfBusiness = datetime.strptime('4:00 PM', '%I:%M %p')
startOfBusiness = datetime.strptime('8:00 AM', '%I:%M %p')

hash = HashTable()


#update status packages on truck
def updatePkgsStatus(timeObj, truck):
    truck.packagesOnTruck = truck.orderPackagesByRoute()
    pkgsOnTruck = truck.packagesOnTruck.copy()
    timeDif = (timeObj - truck.departureTime)
    milesTraveled = (timeDif.total_seconds()/3600)*18
    truck.milesDriven = milesTraveled
    mileage = 0
    
    if timeObj < truck.departureTime:
        for pkg in pkgsOnTruck:
            status = "at the hub: " + str(timeObj)
            hash.update(pkg.packageID, status)
            
    def caculateDeliveryTime(mileage, departureTime):
        startTime = departureTime
        timePassed = (mileage/18)*60
        duration = timedelta(minutes=timePassed)
        return startTime + duration
    
    for i in range(len(truck.orderedDistances)):
        mileage += truck.orderedDistances[i]
        address = truck.route[i+1]
        deliveryTime = caculateDeliveryTime(mileage, truck.departureTime)

        if mileage < milesTraveled:
            while 0 < len(pkgsOnTruck):
                pkg = pkgsOnTruck[0]
                if address == pkg.address:
                    pkgsOnTruck.pop(0)
                    status = "delivered: " + str(deliveryTime)
                    hash.update(pkg.packageID, status)
                    truck.numPackages -= 1
                    continue
                break

        else:
            for pkg in pkgsOnTruck:
                pkg = pkgsOnTruck.pop(0)
                status = "en route: " + str(timeObj)
                hash.update(pkg.packageID, status)

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

updatePkgsStatus(timeObj, truck1)
updatePkgsStatus(timeObj, truck2)
updatePkgsStatus(timeObj, truck3)

print('\n1. Look up a Package')
print('2. View All Packages\n')


while True:
    num = input('What would you like to do? Type 1 or 2\n')
    try:
        num == '1' or num == '2'
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
    print(hash.find(pid))

if num == '2':
    print(f"Truck 1: \n{truck1}")
    for pkgs in truck1Pkgs:
        pid = pkgs.packageID
        print(f"{hash.find(pid)} \n")
    print(f"Truck 2: \n{truck1}")
    for pkgs in truck2Pkgs:
        pid = pkgs.packageID
        print(f"{hash.find(pid)} \n")
    print(f"Truck 3: \n{truck2}")
    for pkgs in truck3Pkgs:
        pid = pkgs.packageID
        print(f"{hash.find(pid)} \n")
        










