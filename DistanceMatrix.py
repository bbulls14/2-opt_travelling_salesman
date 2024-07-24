import csv
from datetime import datetime
from Clock import Clock

class Vertex:
    def __init__(self, address, index):
        self.address = address
        self.index = index
        self.next = None

class Matrix:
    def __init__(self):
        self.vertices = {} #{k = vertex.address, v = index of row in csvFile}
       
        #SpaceComplexity: O(v^2), v = number of vertices in self.vertices
        self.edges = [] #2d array of distances
        
        self.edgeIndices = {} #{k = address, v = index in self.edges}
        self.reverseEdgeIndices = {} #{k = index in self.edges, v = address}
        self.deadlines = {} #{k = address, v = deadline(datetime object)}
        
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
    #Time Complexity: O(r*(v+e)) + O(v^2), Space Complexity: O(v^2) + O(r*c)
    #       a. r = number of rows in csvFile, c = number of columns in csvFile, v = number of vertices, e = len(self.edges)
    def matrixAttributes(self, listOfPackages):
        self.createMatrixSetEdgeIndicesToAddress(listOfPackages)
        return self
        
        
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
    #Time Complexity(r*(v+e)), Space Complexity: O(v^2) from edges being a 2d array of vertices
    #       a. r = number of rows in csvFile, c = number of columns in csvFile, v = number of vertices, e = len(self.edges)
    #       b. Time/Space Complexity including updateMatrixWithEdgeWeight()
    #               i. Time: O(r*(v+e)) + O(v^2), Space: O(v^2) + O(r*c)
    def createMatrixSetEdgeIndicesToAddress(self, listOfPackages):
        for pkg in listOfPackages: #Time Complexity: O(n) 
            deadline = pkg.deadline
            if pkg.address in self.deadlines: #Time complexity O(1) b/c dict
                if deadline < self.deadlines[pkg.address]:
                    self.deadlines[pkg.address] = deadline #using avg case, Time Complexity: O(1)
                    continue
                else:
                    continue
            self.deadlines[pkg.address] = deadline 
        
        listOfVertices = [getattr(obj, 'address') for obj in listOfPackages] #Time Complexity O(n), Space Complexity: O(v)
        listOfVertices.append('HUB')
        
        #Time Complexity(r*(v+e)), Space Complexity: O(v^2) from edges being a 2d array of vertices
        with open('Wgups Distances.csv', mode='r', encoding='UTF-8-sig') as file:
            csvFile = csv.reader(file, delimiter=',')
            for row in csvFile: #Time/Space Complexity: O(r)
                vertex = row[0]
                index = row[1]
###lines 78-84, 108-129 - (Oggi AI - Artificial Intelligence Today, 2016)    
                if vertex in listOfVertices: #Time Complexity O(v)
                    vertex = Vertex(vertex,index) 
                    self.vertices[vertex.address] = vertex.index #Space Complexity O(v)
                    for row in self.edges: #Time Complexity O(e)
                        row.append(0)
                    self.edges.append([0] * (len(self.edges)+1)) #Space Complexity: O(v^2) b/c 2d array
                    self.edgeIndices[vertex.address] = len(self.edgeIndices) #Time complexity: O(1), Space Complexity: O(v)
        self.reverseEdgeIndices = {address: index for index, address in self.edgeIndices.items()} #Time/Space Complexity: O(v)
        
        self.updateMatrixWithEdgeWeight() #Time Complexity: O(n^2), Space Complexity: O(v+(r*c))
    
    #Flow: 1.called by createMatrixSetEdgeIndices() when creating a local distance matrix with matrixAttributes() 
    #      2.calls addEdge() when updating matrix
    #process: 
    # 1. Create lists of address and index from self.vertices 
    # 2. Use these lists to iterate through Distances csv file and only obtain relevant edgeWeight 
    #       a. keep track of zeroEdge to create mirror along it (this is where address and index reference themselves (e.g. (0,0), (1,1), (2,2))) 
    #       b. find edgeWeight and call addEdge() 
    #       c. set vertexIndex to None to prevent referencing it again
    #Time Complexity: O(v^2), Space Complexity: O(v+(r*c))
    #       a. v = number of vertices, r = number of rows in csvFile, c = number of columns in csvFile
    #       b. includes addEdge(), which has a Time/Space Complexity: O(1)
    def updateMatrixWithEdgeWeight(self):
###lines 108-129 - (Oggi AI - Artificial Intelligence Today, 2016)  
        vertexAddress = list(self.vertices.keys()) #Time/Space Complexity O(v)
        vertexIndex = list(self.vertices.values()) #Time/Space Complexity O(v)

        with open('WGUPS Distances.csv', mode='r', encoding='UTF-8-sig') as file:
            csvFile = list(csv.reader(file, delimiter=',')) #Time/Space Complexity: O(r*c)
            zeroEdge=0
            for i in range(len(vertexIndex)): #Time complexity: O(v)
                
                index1 = int(vertexIndex[i])   
                if index1 is not None and str(index1) in csvFile[index1-1][1]: #Time Complexity generally O(1) b/c value is small and bounded
                    
                    for j in range(len(vertexIndex)): #Time Complexity: O(v)
                        if vertexIndex[j] == None:
                            continue
                        
                        index2 = int(vertexIndex[j])
                        
                        #if both indices are equal, then they reference themselves, so set value to 0
                        if index1 == index2:
                            weight = float(0)
                            self.addEdge(vertexAddress[zeroEdge], vertexAddress[zeroEdge], weight) #Time/Space Complexity: O(1)
                            zeroEdge+=1
                            continue
                        else:
                            #decrement index2 because rows in csvfile start at 0 and index2 starts at 1
                            #increment index1 because columns in csvfile are offset by 1 due to index column
                            weight = float((csvFile[index2-1][index1+1]))
                        self.addEdge(vertexAddress[i], vertexAddress[j], weight) #Time/Space Complexity: O(1)
                        
                    vertexIndex[i] = None

    #flow: called by updateMatrixWithEdgeWeight() when creating a local distance matrix with matrixAttributes()
    #process: 
    # 1. verify that address is in self.vertices 
    # 2. update weight in self.edges using indices from edgeIndices that have the address (e.g. u, v) as the key 
    # 3. update itself and its mirror (e.g. (0,1)==(1,0), (2,5)==(5,2)) with weight from Distances csvFile
    #Time/Space Complexity: O(1)
###lines 140-146 - (Oggi AI - Artificial Intelligence Today, 2016)    
    def addEdge(self, u, v, weight):
        if u in self.vertices and v in self.vertices: #Time Complexity: O(1) b/c dict
            self.edges[self.edgeIndices[u]][self.edgeIndices[v]] = weight
            self.edges[self.edgeIndices[v]][self.edgeIndices[u]] = weight #Time Complexity: O(1) for setting item in list and dict
            return True
        else:
            return False


###lines 201-220 - (2-Opt Algorithm to Solve the Travelling Salesman Problem in Python, n.d.)
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
    #Time Complexity: O(m*n^3), Space Complexity: O(v+n)
    #       b. m = number of times while loop iterates, n = length of tour, v = number of vertices which is equal to len(edgeIndices)
    #       a. space complexity takes into account the addressesFromTour() function called at the end 
    def bestTour(self, truck):
        tour = list(self.edgeIndices.values()) #Time/Space Complexity: O(v)
        
        n = len(tour)
        
        def calculateTourDistance(tour): #Time Complexity: O(n), Space Complexity: O(1)
            totalDistance = 0
            for i in range(n):
                totalDistance += self.edges[tour[i]][tour[(i + 1) % n]]
            return totalDistance
        
        #check if the tour meets all deadline requirements for packages in the tour.
        def meetDeadline(tour): #Time Complexity: O(n)
            endOfBusiness = datetime.strptime('4:00 PM', '%I:%M %p')
            tenThirtyDeadline = datetime.strptime('10:30 AM', '%I:%M %p')
            nineAMDeadline = datetime.strptime('9:00 AM', '%I:%M %p')
            startTime = truck.departureTime
            clock = Clock(startTime)
            
            distanceTraveled = 0
            #Time Complexity: O(n)
            for i in range(n-1): 
                distance = self.edges[tour[i]][tour[(i + 1) % n]] #Time/Space Complexity: O(1)
                distanceTraveled += distance
                clock.addMinutes((distance/18)*60)
                
                deadline = self.deadlines[self.reverseEdgeIndices[tour[i+1]]] #Time/Space Complexity: O(1)

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
###lines 218-242 - (2-Opt Algorithm to Solve the Travelling Salesman Problem in Python, n.d.)        
        improved = True
        while improved: #Time Complexity O(m), difficult to determine b/c depends on tour and distances 
            improved = False
            #start range at 1 so that 0 is always start and end
            for i in range(1, n-1): #Time Complexity: O(n)
                for j in range(i + 1, n): #Time Complexity: O(n)

                    # Create a new tour by swapping i and j
                    newTour = tour[:i] + tour[i:j + 1][::-1] + tour[j + 1:] #Time Complexity: O(n)
                    
                    newDistance = calculateTourDistance(newTour) #Time Complexity: O(n)
                    
                    if newDistance < bestDistance: #Time Complexity: O(n)
                        tour = newTour
                        currentDistance = newDistance
                        
                        if meetDeadline(newTour):    
                            bestTour = newTour
                            bestDistance = newDistance

                            improved = True
        
        for i in range(n): #Time/Space Complexity: O(n)
            distance = self.edges[bestTour[i]][bestTour[(i + 1) % n]]
            truck.orderedDistances.append(distance)  
        
        tourAddresses = self.addressesFromTour(bestTour) #Time/Space Complexity: O(v+n)              
        truck.route = tourAddresses
        truck.milesDriven = bestDistance
        return tourAddresses

    #flow: called at end of bestTour() in AdjMatrix.py
    #process: 
    #   1. creates a list of addresses from the keys used in self.edgeIndices 
    #   2. iterate through tour which is a list of ordered indices that are the values from edgeIndices
    #   3. update addressTour [] with the address at the corresponding index from tour
    #Time/Space Complexity: O(v+n)
    def addressesFromTour(self, tour):
        addresses = list(self.edgeIndices.keys()) #Time and Space Complexity: O(v)
        addressTour = [] #Space Complexity: O(n)
        for index in tour: #Time Complexity: O(n)
            addressTour.append(addresses[int(index)])
        return addressTour    
    

            
     

                    

        
        

        
        

        
