from datetime import datetime
from Package import Package
from AdjMatrix import Matrix
from Truck import Truck

class Logistics:
    def __init__(self):
        # self.graph = graph
        # self.hash_table = hash_table
        self.trucks = {}
        self.allPackages = Package.getPackageDataList() 

        
    def organizePackages(self):
        endOfBusiness = datetime.strptime('4:00 PM', '%I:%M %p')
        tenThirtyDeadline = datetime.strptime('10:30 AM', '%I:%M %p')
        nineAMDeadline = datetime.strptime('9:00 AM', '%I:%M %p')
        
        copyOfAllPackages = self.allPackages.copy()
        
        onlyTruck2 = []
        delayedOnFlight = []
        mustBeTogether = []
        byTenThirty = []
        remainingPkgs = []
        
        index = 0
        while index < len(copyOfAllPackages):
            package = copyOfAllPackages[index]
            address = package.address
            deadline = package.deadline
            specialNote = package.specialNote
            pID = int(package.packageID)
            
            if 'truck 2' in specialNote or address in [p.address for p in onlyTruck2]:
                onlyTruck2.append(copyOfAllPackages.pop(index))
                continue
                
            if 'Delayed on flight' in specialNote or address in [p.address for p in delayedOnFlight]:
                delayedOnFlight.append(copyOfAllPackages.pop(index))
                continue

            if 'Must be delivered with' in specialNote or pID in {13, 15, 19} or address in [p.address for p in mustBeTogether]:
                mustBeTogether.append(copyOfAllPackages.pop(index))
                continue
            
            if deadline < endOfBusiness or address in [p.address for p in byTenThirty]:
                byTenThirty.append(copyOfAllPackages.pop(index))
                continue
            index += 1
            
        remainingPkgs = [p for p in copyOfAllPackages]        
            
            
        return onlyTruck2, delayedOnFlight, mustBeTogether, byTenThirty, remainingPkgs
          
    # def mapAddressToDistance    
                
 
    def choosePackagesForTruck(self):
        matrix = Matrix()
        t2, flight, together, tenThirty, leftOvers = self.organizePackages()
        matrix1 = matrix.matrixAttributes(t2)
        
 
        Truck1 = []
        Truck2 = []
        Truck3 = []
        
        tour, distance = matrix1.bestPathWith()
        
        #adjust 2optalgo to accept 2 lists, it will add edges from another list and swap them to determin the best path.         

if __name__ == "__main__":
    logistics = Logistics()

    
    logistics.choosePackagesForTruck()
    print('DONE')
 