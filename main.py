from HashTable import HashTable
from AdjMatrix import Matrix
from Package import Package
from Truck import Truck

pkg = Package()

matrix1 = Matrix()
matrix2 = Matrix()
matrix3 = Matrix()

truck1Pkgs, truck2Pkgs, truck3Pkgs = pkg.organizePackages()

truck1 = Truck(truck1Pkgs)
truck2 = Truck(truck2Pkgs)
truck3 = Truck(truck3Pkgs)

matrix1 = matrix1.matrixAttributes(truck1.packagesOnTruck)
matrix2 = matrix2.matrixAttributes(truck2.packagesOnTruck)
matrix3 = matrix3.matrixAttributes(truck3.packagesOnTruck)



tour1, distance1 = matrix1.bestPath(truck1)
tour2, distance2 = matrix2.bestPath(truck2)
tour3, distance3 = matrix3.bestPath(truck3)
print('DONE')



