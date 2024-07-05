import csv
import heapq
from Package import Package

startVertex = '4001 South 700 East'

class Vertex:
    def __init__(self, n):
        self.name = n

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []
        self.edgeIndices = {}
        self.getVertexData()
        self.getEdgeWeight()

    def getVertexData(self):
        with open('Wgups Distances.csv', mode='r', encoding='UTF-8-sig') as file:
            csvFile = csv.reader(file, delimiter=',')
            for row in csvFile:
                vertex = row[0]  
                self.addVertex(Vertex(vertex))

    def addVertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges) + 1))
            
            self.edgeIndices[vertex.name] = len(self.edgeIndices)
            
            return True
        else:
            return False
        
    def getEdgeWeight(self):
        vertexName = list(self.vertices.keys())
        
        with open('WGUPS Distances.csv', mode='r', encoding='UTF-8-sig') as file:
            csvFile = list(csv.reader(file, delimiter=','))
            for i, row in enumerate(csvFile):
                for j, value in enumerate(row):
                    if j == 0:
                        continue
                    if value:
                        weight = float(value)
                    else:
                        weight = 0  
                    if weight != 0:
                        self.addEdge(vertexName[i], vertexName[j-1], weight)
                    
    def addEdge(self, u, v, weight):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edgeIndices[u]][self.edgeIndices[v]] = weight
            self.edges[self.edgeIndices[v]][self.edgeIndices[u]] = weight
            return True
        else:
            return False

    def printGraph(self):
        print("Graph vertices and adjacency matrix:")
        for vertex, index in self.edgeIndices.items():
            print(f"Vertex: {vertex}")
        print("\nAdjacency matrix:")
        for row in self.edges:
            print(' '.join(map(str, row)))

    
    def dijkstra(self):
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[startVertex] = 0
        pq = [(0, startVertex)]
    
        while pq:
            currentDistance, currentVertex = heapq.heappop(pq)
            # print(f"Processing vertex: {currentVertex} with current distance: {currentDistance}")
        
            for neighborIndex, weight in enumerate(self.edges[self.edgeIndices[currentVertex]]):
                if weight > 0: 
                    neighborVertex = list(self.edgeIndices.keys())[neighborIndex]
                    distance = currentDistance + weight
                    # print(f"Checking neighbor: {neighborVertex}, weight: {weight}, calculated distance: {distance}")
                
                    if distance < distances[neighborVertex]:
                        distances[neighborVertex] = distance
                        heapq.heappush(pq, (distance, neighborVertex))
                        # print(f"Updated distance for {neighborVertex}: {distance}")
    
        rounded_distances = {vertex: round(dist, 1) for vertex, dist in distances.items()}
        return rounded_distances

        

        
    
        
        
    
             
            
        
    


    #     for i in range(7, len(data)):
    #         addresses = data.iloc[i, 0]
    #         self.graph[addresses] = {}
            
    #         for j in range (i, len(data)):
    #             neighbors = data.iloc[i, 0] 
    #             distance = data.iloc[j, i-5]
    #             reverseEdge = {}
                
    #             if addresses != neighbors and pd.notna(distance):
    #                 self.graph[addresses][neighbors] = distance
    #                 reverseEdge
                    
    #                 if neighbors not in self.graph:
    #                     self.graph[neighbors] = {}
    #                 self.graph[addresses][neighbors] = distance
        
    #         # print(f"Address: {self.graph[addresses]}")                
            
    # def addReverseEdge(self):
                
            
        

        
        

        
