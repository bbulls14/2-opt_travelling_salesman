import csv
from datetime import datetime
from Truck import Truck
from Clock import Clock

class Vertex:
    def __init__(self, address, index):
        self.address = address
        self.index = index
        self.next = None

class Matrix:
    def __init__(self):
        self.vertices = {}
        self.edges = []
        self.edgeIndices = {}
        self.reverseEdgeIndices = {}
        self.deadlines = {}
        
    def printMatrix(self):
        print("Graph vertices and adjacency matrix:")
        for vertex in self.edgeIndices.items():
            print(f"Vertex: {vertex}")
        print("\nAdjacency matrix:")
        for row in self.edges:
            print(' '.join(map(str, row)))

    #flow: called from main.py after HashTable initialized and packages are organized onto trucks
    #process: 
    # 1. calls chain of functions (createMatrixSetEdgeIndicesToAddress(), updateMatrixWithEdgeWeight(), addEdge()) 
    # 2. returns an updated local Distance Matrix
    def matrixAttributes(self, listOfPackages):
        self.createMatrixSetEdgeIndicesToAddress(listOfPackages)
        return self
        
        
#referenced lines (50-77, 87-118, and 125 - 131) from Oggi AI at 6:26-8:43 of https://www.youtube.com/watch?v=HDUzBEG1GlA&t=486s    
    #flow: called by matrixAttributes in DistanceMatrix.py 
    # 1. initializes dictionary with addresses and deadlines from listOfPackages arg
    #          a. this is referenced in meetDeadline() which is an embedded function within bestTour() in DistanceMatrix.py 
    # 2. create a list of addresses from the listOfPackages, add 'HUB' to use as start and end point of route 
    # 3. open Distances csv file, iterate through rows 
    #          b. for each row extract the address and index within csvFile, verify that address is in listOfVertices, initialize vertex object whith address and index
    #          c. store these vertex attributes in self.vertices with vertex.address as key, and vertex.index as value 
    #          d. extend rows and columns of self.edges by 1 for each iteration 
    #          e. store the vertex location within self.edges in self.edgeIndices, set key to vertex.address and value to the row/column that vertex resides at
    # 4. create a reversed dictionary of edgeIndices, to more easily reference in meetDeadline() 
    # 5. call updateMatrixWithEdgeWeight()
    def createMatrixSetEdgeIndicesToAddress(self, listOfPackages):
        for pkg in listOfPackages:
            deadline = pkg.deadline
            if pkg.address in self.deadlines:
                if deadline < self.deadlines[pkg.address]:
                    self.deadlines[pkg.address] = deadline
                    continue
                else:
                    continue
            self.deadlines[pkg.address] = deadline
        
        listOfVertices = [getattr(obj, 'address') for obj in listOfPackages]
        listOfVertices.append('HUB')
        
        with open('Wgups Distances.csv', mode='r', encoding='UTF-8-sig') as file:
            csvFile = csv.reader(file, delimiter=',')
            for row in csvFile:
                vertex = row[0]
                index = row[1]
                if vertex in listOfVertices:
                    vertex = Vertex(vertex,index)
                    self.vertices[vertex.address] = vertex.index 
                    for row in self.edges: 
                        row.append(0)
                    self.edges.append([0] * (len(self.edges)+1))
                    self.edgeIndices[vertex.address] = len(self.edgeIndices)
        self.reverseEdgeIndices = {address: index for index, address in self.edgeIndices.items()}
        self.updateMatrixWithEdgeWeight()
    
    #Flow: 1.called by createMatrixSetEdgeIndices() when creating a local distance matrix with matrixAttributes() 
    #      2.calls addEdge() when updating matrix
    #process: 
    # 1. Create lists of address and index from self.vertices 
    # 2. Use these lists to iterate through Distances csv file and only obtain relevant edgeWeight 
    #       a. keep track of zeroEdge to create mirror along it (this is where address and index reference themselves (e.g. (0,0), (1,1), (2,2))) 
    #       b. find edgeWeight and call addEdge() 
    #       c. set vertexIndex to None to prevent referencing it again
    def updateMatrixWithEdgeWeight(self):

        vertexAddress = list(self.vertices.keys())
        vertexIndex = list(self.vertices.values())

        with open('WGUPS Distances.csv', mode='r', encoding='UTF-8-sig') as file:
            csvFile = list(csv.reader(file, delimiter=','))
            zeroEdge=0
            for i in range(len(vertexIndex)):
                
                index1 = int(vertexIndex[i])   
                if index1 is not None and str(index1) in csvFile[index1-1][1]:
                    
                    for j in range(len(vertexIndex)):
                        if vertexIndex[j] == None:
                            continue
                        
                        index2 = int(vertexIndex[j])
                        
                        #if both indices are equal, then they reference themselves, so set value to 0
                        if index1 == index2:
                            weight = float(0)
                            self.addEdge(vertexAddress[zeroEdge], vertexAddress[zeroEdge], weight)
                            zeroEdge+=1
                            continue
                        else:
                            #decrement index2 because rows in csvfile start at 0 and index2 starts at 1
                            #increment index1 because columns in csvfile are offset by 1 due to index column
                            weight = float((csvFile[index2-1][index1+1]))
                        self.addEdge(vertexAddress[i], vertexAddress[j], weight)
                        
                    vertexIndex[i] = None

    #flow: called by updateMatrixWithEdgeWeight() when creating a local distance matrix with matrixAttributes()
    #process: 
    # 1. verify that address is in self.vertices 
    # 2. update weight in self.edges using indices from edgeIndices that have the address (e.g. u, v) as the key 
    # 3. update itself and its mirror (e.g. (0,1)==(1,0), (2,5)==(5,2)) with weight from Distances csvFile
    def addEdge(self, u, v, weight):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edgeIndices[u]][self.edgeIndices[v]] = weight
            self.edges[self.edgeIndices[v]][self.edgeIndices[u]] = weight
            return True
        else:
            return False


#referenced lines (201-220) from rrz0 at https://stackoverflow.com/questions/53275314/2-opt-algorithm-to-solve-the-travelling-salesman-problem-in-python
    #flow:called from main.py after trucks are loaded and weighted local adj matrix is made 
    #  
    #process: 
    # 1. create initial tour using existing edgeIndices (e.g. 0,1,2,3,4,5,etc.) 
    # 2. currentDistance is set using calculateTourDistance 
    # 3. bestTour, and bestDistance are set to tour and currentDistance, these values will only update if deadlines are met in a tour and distances are shorter 
    # 4. two-opt algorithm reverses segment between i and j
    #       a. calculates total distance of newTour 
    #       b. if it meets deadlines then tour and current distance are reassigned values of newTour and it's distance
    #       c. If distance of new tour is less than bestDistance, bestTour and bestDistance are updated with values from newTour and newDistance
    #            i. improved is set to True and the algorithm reiterates with the tour now starting over from bestTour and bestDistance
    # 5. update truck object
    #       a. truck.orderedDistances is update with a list of distances as they're traveled in the route
    #       b. truck.route is update with ordered list of addresses according to route of bestTour
    #       c. truck.milesDriven is updated with total distance traveled in bestTour
    def bestTour(self, truck):
        tour = list(self.edgeIndices.values())
        
        n = len(tour)
        
        def calculateTourDistance(tour):
            totalDistance = 0
            for i in range(n):
                totalDistance += self.edges[tour[i]][tour[(i + 1) % n]]
            return totalDistance
        
        #check if the tour meets all deadline requirements for packages in the tour.
        def meetDeadline(tour):
            endOfBusiness = datetime.strptime('4:00 PM', '%I:%M %p')
            tenThirtyDeadline = datetime.strptime('10:30 AM', '%I:%M %p')
            nineAMDeadline = datetime.strptime('9:00 AM', '%I:%M %p')
            startTime = truck.departureTime
            clock = Clock(startTime)
            
            distanceTraveled = 0

            for i in range(n-1):
                distance= self.edges[tour[i]][tour[(i + 1) % n]]
                distanceTraveled += distance
                clock.addMinutes((distance/18)*60)
                
                deadline = self.deadlines[self.reverseEdgeIndices[tour[i+1]]]

                if deadline <= nineAMDeadline:
                    if clock.getTime() <= nineAMDeadline:
                        continue
                    else:
                        return False
                if deadline <= tenThirtyDeadline:
                    if clock.getTime() <= tenThirtyDeadline:
                        continue
                    else:
                        return False
                if deadline <= endOfBusiness:
                    if clock.getTime() <= endOfBusiness:
                        continue
                    else:
                        return False
            return True  
              
        currentDistance = calculateTourDistance(tour)

        bestTour = tour
        bestDistance = currentDistance
        
        improved = True
        while improved:
            improved = False
            for i in range(1, n - 1): #start range at 1 so that 0 is always start and end
                for j in range(i + 1, n):
                    if j - i == 1:
                        continue # Skip adjacent edges

                    # Create a new tour by reversing the segment between i and j
                    newTour = tour[:i] + tour[i:j + 1][::-1] + tour[j + 1:]
                    
                    newDistance = calculateTourDistance(newTour)
                    
                    if meetDeadline(newTour):
                        tour = newTour
                        currentDistance = newDistance
                        
                        if newDistance < bestDistance:
                            bestTour = newTour
                            bestDistance = newDistance

                            improved = True
        
        for i in range(n-1):
            distance = self.edges[bestTour[i]][bestTour[(i + 1) % n]]
            truck.orderedDistances.append(distance)  
        
        tourAddresses = self.addressesFromTour(bestTour)                 
        truck.route = tourAddresses
        truck.milesDriven = bestDistance
        return tourAddresses

    #flow: called at end of bestTour() in AdjMatrix.py
    #process: 
    #   1. creates a list of addresses from the keys used in self.edgeIndices 
    #   2. iterate through tour which is a list of ordered indices that are the values from edgeIndices
    #   3. update addressTour [] with the address at the corresponding index from tour
    def addressesFromTour(self, tour):
        addresses = list(self.edgeIndices.keys())
        addressTour = []
        for index in tour:
            addressTour.append(addresses[int(index)])
        return addressTour    
    

            
     

                    

        
        

        
        

        
