from datetime import datetime
from HashTable import HashTable
from AdjMatrix import Matrix
from Package import organizePackages
from Truck import Truck



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



tour1, distance1 = matrix1.bestPath(truck1)
tour2, distance2 = matrix2.bestPath(truck2)
tour3, distance3 = matrix3.bestPath(truck3)


print('*******************************************************************************\n')

print('Welcome to the WGUPS Delivery Interface\n')


print('1. Check the status of a package')
print('2. Check miles traveled by a truck')
input('What would you like to do? Type 1, 2, or 3\n')
# input = int(input)

# if input != 1 or input !=2:
    


timeOK = True
while timeOK:
    try:
        time = input("What time is it? __:__ AM/PM\n")
        timeObj = datetime.strptime(time, "%I:%M %p")
    except:
        print("\nInvalid Input, use the correct format for hour and minute.\nDon't forget the ':' and include AM or PM at the end\n")
        timeOK = True
    else:
        timeOK = False












