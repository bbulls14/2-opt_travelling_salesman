### Blake Bulls 011249334

from datetime import datetime, timedelta
from HashTable import HashTable
from DistanceMatrix import Matrix
from Package import organizePackages
from Truck import Truck

 

#Flow: HashTable is initialized with package data obtained from Package.py
#process: 
# 1. call getPackageData() from package.py upon initialization
# 2. iterate through hashPackageData and insert packages using the packageID as the key
#       a. reference hashPackageData to update buckets with required values
hash = HashTable()


#flow: uses timeObj input and truck object to update pkg status in hashTable and truck objects
#proces: 
# 1.organize packages by route 
# 2. check if timeObj is later than truck's departure time, 
#           a. if so calculate timeDif
#           b. otherwise, the truck hasn't left the hub so set all packages' status to 'at the hub' + timeObj
# 3. calculate milesTraveled from timeObj
# 4. check if milesTraveled are less than the truck.milesDriven (its current value is bestTour distance)
#           a. update truck.milesDriven to approproiate miles traveled based on timeObj
#5. check if milesTraveled is greater than truck.milesDriven( value = bestTour distance)
#           b. update milesTraveled so that it doesn't exceed total milesDriven
#6. iterate through ordered distances, update mileage upon each iteration.
#           a. if mileage is less than milesTraveled the package was delivered, its status and time are updated
#           b. otherwise, its status is en route and time is set to timeObj
#Time Complexity is O(m * n), Space Complexity depends on timeObj, 
#       a. m = number of routes in truck.routes, n = number of packages on truck
#       b. if timeObj < truck.departureTime -> Time Complexity: O(m*n), Space Complexity: O(n) because it doesn't need to access orderedDistances list
#       c. if timeObj is > truck.departure time -> the orderedDistance for loop has a Time/Space Complexity: O(m*n)
#           i. truck.orderPackagesByRoute() has time complexity O(m * n) because it iterates through routes and packagesOnTruck, which vary in length
#               ii.the truck.orderedDistances for loop is also O(m * n) because orderedDistances is equal to route - 1 (route includes 'HUB'). 
def updatePkgsStatus(timeObj, truck):
    truck.packagesOnTruck = truck.orderPackagesByRoute() #Time complexity: O(m*n), SpaceComplexity: O(n)
    pkgsOnTruck = truck.packagesOnTruck.copy() #Time/Space Complexity: O(n)
    
    if timeObj >= truck.departureTime:   
        timeDif = (timeObj - truck.departureTime)
    else:
        truck.milesDriven = 0
        for pkg in pkgsOnTruck: #Time/Space Complexity: O(n)
            pkg.status = "at the hub " + timeObj.strftime('%I:%M %p')
            hash.update(pkg.packageID, pkg) #Time/Space Complexity: O(1)
        return
    
    milesTraveled = (timeDif.total_seconds()/3600)*18
    mileage = 0

    if milesTraveled <= truck.milesDriven: truck.milesDriven = milesTraveled
    if milesTraveled > truck.milesDriven: milesTraveled = truck.milesDriven 
   
        
    
    def caculateDeliveryTime(mileage, departureTime): #Time/Space Complexity: O(1)
        startTime = departureTime
        timePassed = (mileage/18)*60
        duration = timedelta(minutes=timePassed)
        return startTime + duration
    
    for i in range(len(truck.orderedDistances)): #Time/Space Complexity: O(m * n)
        mileage += truck.orderedDistances[i]
        address = truck.route[(i+1)%len(truck.route)] 
        deliveryTime = caculateDeliveryTime(mileage, truck.departureTime)
        if address == 'HUB' and len(pkgsOnTruck) == 0:
            truck.returnedTime = deliveryTime
        if mileage < milesTraveled:
            while 0 < len(pkgsOnTruck):
                pkg = pkgsOnTruck[0]
                if address == pkg.address:
                    pkgsOnTruck.pop(0)
                    pkg.status = "delivered " + deliveryTime.strftime('%I:%M %p')
                    hash.update(pkg.packageID, pkg)
                    continue
                break

        else:
            for pkg in pkgsOnTruck:
                pkg = pkgsOnTruck.pop(0)
                pkg.status = "en route " + timeObj.strftime('%I:%M %p')
                hash.update(pkg.packageID, pkg)
    
#initialize empty matrix
matrix1 = Matrix()
matrix2 = Matrix()
matrix3 = Matrix()

print('*******************************************************************************\n')

print('Welcome to the WGUPS Delivery Interface\n')

while True:
    try:
        time = input("What time is it? __:__ AM/PM\n")
        timeObj = datetime.strptime(time, "%I:%M %p")
        break              
    except:
        print("\nInvalid Input, use the correct format for hour and minute.\nDon't forget the ':' and include AM or PM at the end\n")
#initialize empty Trucks
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

#flow: calls organizePackages() in Packages.py
#process: 
# 1. loads trucks with packages according to their requirements
# 2. Uses timeObj to update hashtable and truck.packagesOnTruck if package attribute is time-sensitive (e.g. Delayed on Flight, Wrong address)
#Time Complexity O(n^3) from both while loops, list.pop(arg), hash.update(), Space Complexity: O(n), n = len(allPackages)
organizePackages(hash, timeObj, truck1, truck2, truck3)

#flow: calls matrixAttributes() using organized truck.packagesOnTruck arg
#process: creates a distance matrix only using distances for addresses of packages on truck
#Time Complexity(r*(v+e)), Space Complexity: O(v^2) from edges being a 2d array of vertices
matrix1 = matrix1.matrixAttributes(truck1.packagesOnTruck)
matrix2 = matrix2.matrixAttributes(truck2.packagesOnTruck)
matrix3 = matrix3.matrixAttributes(truck3.packagesOnTruck)

#flow: calls bestTour() using truck arg
#process: 
# 1. calculates bestTour using two-opt algorithm 
# 2. returns ordered lists of addresses according to bestTour
#       a. updates truck.milesDriven to be equal to total distance of bestTour 
#       b. updates truck.orderedDistances to be an ordered lists of miles to each address
#       c. updates truck.route to be an ordered list of addresses traveled in bestTour
#Time Complexity: O(m*n^3), Space Complexity: O(v+n)
matrix1.bestTour(truck1)
matrix2.bestTour(truck2)
matrix3.bestTour(truck3)

#flow: call updatePkgsStatus() in main.py using timeObj and truck object
#process: 
# 1. update status of packages on truck according to timeObj, package attributes, and truck route
#Time Complexity is O(m * n), Space Complexity depends on timeObj, 
updatePkgsStatus(timeObj, truck1)
updatePkgsStatus(timeObj, truck2)

#only update truck3 if truck1 or truck2 returned before truck3's departure time
unableToDeliver = True
if truck1.returnedTime <= truck3.departureTime or truck2.returnedTime <= truck3.departureTime:
    updatePkgsStatus(timeObj, truck3)
    unableToDeliver = False
 

print('\n1. Look up a Package')
print('2. View All Packages\n')


while True:
    num = input('What would you like to do? Type 1 or 2\n')
    try:
        num == '1' or num == '2'
        break
    except:
        print('Please input either 1 or 2')
#find 1 package using packageID as key in HashTable
if num == '1':
    while True:
        print('\nChecking the status of a package.....')
        try:
            pid = input('What is the packageID that you would like to check?\n')
            0 < int(pid) <= hash.used
            break
        except:
            print('Please enter a valid packageID\n')
    print(str(hash.find(pid))) #Time Complexity: O(n) b/c of collision management
    
#print all packages and their totalMiles traveled
#Time Complexity: O(n^2), Space Complexity: O(n)
if num == '2':
    print(f"Truck 1: \n{truck1}")
    for pkgs in truck1.packagesOnTruck:#Time/Space Complexity: O(n)
        pid = pkgs.packageID
        print(f"{str(hash.find(pid))} \n")#Time Complexity: O(n) b/c of collision management
    print(f"Truck 2: \n{truck2}")
    for pkgs in truck2.packagesOnTruck:
        pid = pkgs.packageID
        print(f"{str(hash.find(pid))} \n")
    #only print truck 3 info if it was able to deliver 
    # (i.e. truck1 or truck2 returned to the hub before truck3's departure time)
    if unableToDeliver:
        truck3.milesDriven = 0
        print(f"Truck 3 was unable to deliver due to no drivers available")
    else:
        print(f"Truck 3: \n{truck3}")
        for pkgs in truck3.packagesOnTruck:
            pid = pkgs.packageID
            print(f"{str(hash.find(pid))} \n")
    totalMiles = truck1.milesDriven + truck2.milesDriven + truck3.milesDriven
    print(f"Time: {timeObj.strftime('%I:%M %p')}\nTotal Miles Driven: {"%.2f" % totalMiles}")
        