import csv
import heapq
from Package import Package

HUB = 'HUB'

class Vertex:
    def __init__(self, address):
        self.address = address

class Graph:
    def __init__(self, listOfVertices):
        self.vertices = {}
        self.size = len(listOfVertices)
        self.edges = [[0] * self.size for _ in range(self.size)]
        self.edgeIndices = {}
        self.getVertexData(listOfVertices)
        self.getEdgeWeight()

    def getVertexData(self, listOfVertices):
        with open('Wgups Distances.csv', mode='r', encoding='UTF-8-sig') as file:
            csvFile = csv.reader(file, delimiter=',')
            for row in csvFile:
                vertex = row[0]
                index = row[1]
                if vertex in listOfVertices:
                    self.vertices[index] = vertex
                    self.edgeIndices[vertex] = len(self.edgeIndices)
    

    def getEdgeWeight(self):
        vertexAddress = list(self.vertices.keys())
        
        with open('WGUPS Distances.csv', mode='r', encoding='UTF-8-sig') as file:
            csvFile = list(csv.reader(file, delimiter=','))
            
            for i, row in enumerate(csvFile):
                if row[0] in vertexAddress:
                    for j in range(1, len(row)):
                        if csvFile[0][j] in vertexAddress:
                            value = row[j]
                            if j==0:
                                continue
                            if value:
                                weight = float(value)
                            else:
                                weight = 0  
                            if weight != 0:
                                self.addEdge(vertexAddress[i], vertexAddress[j-1], weight)
                    
    def addEdge(self, u, v, weight):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edgeIndices[u]][self.edgeIndices[v]] = weight
            self.edges[self.edgeIndices[v]][self.edgeIndices[u]] = weight
            return True
        else:
            return False

    def printGraph(self):
        print("Graph vertices and adjacency matrix:")
        for vertex in self.edgeIndices.items():
            print(f"Vertex: {vertex}")
        print("\nAdjacency matrix:")
        for row in self.edges:
            print(' '.join(map(str, row)))

                
            
        

        
        

        
