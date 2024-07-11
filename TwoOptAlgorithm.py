from datetime import datetime
from LocalAdjMatrix import Matrix


class TwoOptAlgorithm():
    def __init__(self, matrix):
        self.matrix = matrix
        self.edges = matrix.edges
        self.edgeIndices = matrix.edgeIndices
        self.reverseEdgeIndices = matrix.reverseEdgeIndices
        self.deadlines = matrix.deadlines
    
    def bestPath(self):
        tour = list((self.edgeIndices.values()))
        n = len(tour)
        tourEdges = [(tour[i-1], tour[i]) for i in range (n)]
        edgeDistances = [self.edges[tour[i - 1]][tour[i]] for i in range(n)]
        

        improved = True
        while improved:
            improved = False
                
            for i in range (n):
                for j in range (i+1,n):
                    cur1 = (tour[i], tour[i+1])
                    cur2 = (tour[j], tour[(j+1)%n])
                    curLength = self.edges[i][i+1] + self.edges[j][(j+1)%n]
                    curPathCost = self.prioritizeDeadline(curLength,cur1, cur2)
                    
                    new1 = (tour[i], tour[j])
                    new2 = (tour[i+1], tour[(j+1)%n])
                    newLength = self.edges[i][j] + self.edges[i+1][(j+1)%n]
                    newPathCost = self.prioritizeDeadline(newLength,new1,new2)
                    
                    if newPathCost < curPathCost:
                        
                        tour[i+1:j+1] = tour[i+1:j+1][::-1]
                        tourEdges = [(tour[i-1], tour[i]) for i in range (n)]
                        edgeDistances = [self.edges[tour[i - 1]][tour[i]] for i in range(n)] 
                           
        tourEdgesWithDistances = dict(zip(tourEdges,edgeDistances))
        orderedEdges, orderedDistances = self.orderedEdgesAndDistances(tourEdges, tourEdgesWithDistances)
        addressPath = self.addressesFromTour(orderedEdges)
        return addressPath, orderedDistances
    
    def prioritizeDeadline(self,length, loc1, loc2):
        totalCost = length

        edge1A1 = self.reverseEdgeIndices.get(loc1[0])
        edge1A2 = self.reverseEdgeIndices.get(loc1[1])
        
        edge2A1 = self.reverseEdgeIndices.get(loc2[0])
        edge2A2 = self.reverseEdgeIndices.get(loc2[1])

        pathAddresses = [edge1A1, edge1A2, edge2A1, edge2A2]

        deadlinePenalty = 0

        for address in pathAddresses:
            if 'HUB' == address:
                continue
            if address in self.deadlines:
                deadline = self.deadlines[address]
                if deadline.time() == datetime.strptime('9:00 AM', '%I:%M %p').time():
                    deadlinePenalty = -2  # 10 units per minute
                elif deadline.time() == datetime.strptime('10:30 AM', '%I:%M %p').time():
                    deadlinePenalty += -2   # 5 units per minute


        totalCost += deadlinePenalty
        return totalCost

            
        # referenced Sylvaus at https://stackoverflow.com/questions/64960368/how-to-order-tuples-by-matching-the-first-and-last-values-of-each-a-b-b-c
    def orderedEdgesAndDistances(self, tourEdges, tourEdgesWithDistances):    
            
        adjMatrix = {edge[0]: edge for edge in tourEdges}
            
        start = 0
            
        orderedEdges = [adjMatrix.pop(start)]
            
        while adjMatrix:
            lastEdge = orderedEdges[-1]
            nextEdge = adjMatrix[lastEdge[1]]
            penaltyLast = self.prioritizeDeadline(0, lastEdge, nextEdge)
            penaltyNext = self.prioritizeDeadline(0, nextEdge, lastEdge)
                
            if penaltyNext < penaltyLast:
                nextEdge = adjMatrix.pop(lastEdge[1])
            else:
                nextEdge = adjMatrix.pop(lastEdge[1])
                orderedEdges.append(nextEdge) 
            
        orderedDistances = []
        for edge in orderedEdges:
            if edge in tourEdgesWithDistances:
                orderedDistances.append(tourEdgesWithDistances[edge])
            
            
        return orderedEdges, orderedDistances  

                    
                    

    def addressesFromTour(self, orderedEdges):
        addresses = list(self.edgeIndices.keys())
        tour = [index for edge in orderedEdges for index in edge]
        addressPath = []
        for index in tour:
            address = addresses[index]
            addressPath.append(address)
        return addressPath    