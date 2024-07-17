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

    #function to build matrix from packageList 
    def matrixAttributes(self, listOfPackages):
        self.createMatrixSetEdgeIndicesToAddress(listOfPackages)
        return self
        
        
    #referenced from Oggi AI at 6:26-8:43 of https://www.youtube.com/watch?v=HDUzBEG1GlA&t=486s
    #self adjusts according to number and attributes of packages that are input
    def createMatrixSetEdgeIndicesToAddress(self, listOfPackages):
        #seperate deadlines into dictionary with address as key to reference in bestPath and meetDeadline functions
        for pkg in listOfPackages:
            deadline = pkg.deadline
            if pkg.address in self.deadlines:
                if deadline < self.deadlines[pkg.address]:
                    self.deadlines[pkg.address] = deadline
                    continue
                else:
                    continue
            self.deadlines[pkg.address] = deadline
        
        #extract addresses from packages in listOfPackages, add 'HUB' to list
        listOfVertices = [getattr(obj, 'address') for obj in listOfPackages]
        listOfVertices.append('HUB')
        
        with open('Wgups Distances.csv', mode='r', encoding='UTF-8-sig') as file:
            csvFile = csv.reader(file, delimiter=',')
            for row in csvFile:
                vertex = row[0]
                index = row[1]
                if vertex in listOfVertices:
                    vertex = Vertex(vertex,index)
                    self.vertices[vertex.address] = vertex.index #store with index to access only needed distances 
                    #extend length and width of matrix for each additional vertices
                    for row in self.edges: 
                        row.append(0)
                    self.edges.append([0] * (len(self.edges)+1))
                    #match vertex address to it's index in the matrix
                    self.edgeIndices[vertex.address] = len(self.edgeIndices)
        #used for deadline list in meetDeadline()
        self.reverseEdgeIndices = {address: index for index, address in self.edgeIndices.items()}
        self.updateMatrixWithEdgeWeight()
    
    #get Edge weight from csv file, and update matrix with values    
    def updateMatrixWithEdgeWeight(self):
        #access addresses and index from vertices dictionary 
        #Use the index to find only necessary values within csv File
        vertexAddress = list(self.vertices.keys())
        vertexIndex = list(self.vertices.values())

        with open('WGUPS Distances.csv', mode='r', encoding='UTF-8-sig') as file:
            csvFile = list(csv.reader(file, delimiter=','))
           #keep track of zeroEdge for mirror of matrix 
            zeroEdge=0
            for i in range(len(vertexIndex)):
                
                index1 = int(vertexIndex[i])   
                #check if index is in csvFile and isn't None
                if index1 is not None and str(index1) in csvFile[index1-1][1]:
                    
                    for j in range(len(vertexIndex)):
                        if vertexIndex[j] == None:
                            continue
                        
                        index2 = int(vertexIndex[j])
                        
                        #if both indices are equal, then they reference themselves, so set value to 0
                        #add zeroEdge and adjust and increment zeroEdge variable           
                        if index1 == index2:
                            weight = float(0)
                            self.addEdge(vertexAddress[zeroEdge], vertexAddress[zeroEdge], weight)
                            zeroEdge+=1
                            continue
                        else:
                            #decrement index2 because rows in csvfile are offset by 1
                            #increment index1 because columns in csvfile are offset by 1 due to index column
                            weight = float((csvFile[index2-1][index1+1]))
                        #update edge to weight found at appropriate index in csv file
                        self.addEdge(vertexAddress[i], vertexAddress[j], weight)
                    #set used index to None to prevent referenceing it again    
                    vertexIndex[i] = None

    #validate that index is in self.vertices
    #update index and it's mirror with weight from csvFile                
    def addEdge(self, u, v, weight):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edgeIndices[u]][self.edgeIndices[v]] = weight
            self.edges[self.edgeIndices[v]][self.edgeIndices[u]] = weight
            return True
        else:
            return False


    #modeled after Austin Buchanan in https://www.youtube.com/watch?v=UAEjUk0Zf90           
    def bestPath(self, truck):
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
            for i in range(1, n - 1):
                for j in range(i + 1, n):
                    if j - i == 1:
                        continue  # Skip adjacent edges

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
        
        orderedDistance = []
        for i in range(n-1):
            distance = self.edges[bestTour[i]][bestTour[(i + 1) % n]]
            orderedDistance.append(distance)  
             
        tourAddresses = self.addressesFromTour(bestTour)                 
        truck.route = tourAddresses
        truck.milesDriven = bestDistance                
        return tourAddresses, orderedDistance

     
    #getIndices function
        # referenced Sylvaus at https://stackoverflow.com/questions/64960368/how-to-order-tuples-by-matching-the-first-and-last-values-of-each-a-b-b-c
    def orderedEdgesAndDistances(tourEdges, tourEdgesWithDistances):    
            
        adjMatrix = {edge[0]: edge for edge in tourEdges}   
        start = 0  
        orderedEdges = [adjMatrix.pop(start)]
            
        while adjMatrix:
            orderedEdges.append(adjMatrix.pop(orderedEdges[-1][1]))
            
        orderedDistances = []
        for edge in orderedEdges:
            if edge in tourEdgesWithDistances:
                orderedDistances.append(tourEdgesWithDistances[edge])  
            
        return orderedDistances


    def addressesFromTour(self, tour):
        addresses = list(self.edgeIndices.keys())
        addressPath = []
        for index in tour:
            addressPath.append(addresses[int(index)])
        return addressPath    
    
            
     

                    

        
        

        
        

        
