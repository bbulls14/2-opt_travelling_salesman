import csv
import heapq
from operator import itemgetter
from Package import Package


class Vertex:
    def __init__(self, address, index):
        self.address = address
        self.index = index
        self.next = None

class Matrix:
    def __init__(self, listOfVertices):
        self.vertices = {}
        self.edges = []
        self.edgeIndices = {}
        self.getVertexData(listOfVertices)

    #lines 21-76 referenced from Oggi AI at 6:26-8:43 of https://www.youtube.com/watch?v=HDUzBEG1GlA&t=486s
    def getVertexData(self, listOfVertices):
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
        self.getEdgeWeight()

    def getEdgeWeight(self):
        vertexAddress = list(self.vertices.keys())
        vertexIndex = list(self.vertices.values())
    
        with open('WGUPS Distances.csv', mode='r', encoding='UTF-8-sig') as file:
            csvFile = list(csv.reader(file, delimiter=','))
            
            zeroEdge=0
            for i in range(len(vertexIndex)):
                
                index1 = vertexIndex[i]
                    
               
                if index1 in csvFile[int(index1)-1][1]:
                    
                    
                    for j in range(len(vertexIndex)):
                        index2 = vertexIndex[j]
                        if index2 == None:
                            continue

                        if index1 == index2:
                            weight = float(0)
                            self.addEdge(vertexAddress[zeroEdge], vertexAddress[zeroEdge], weight)
                            zeroEdge+=1
                            continue
                        
                        weight = float(csvFile[int(index2)-1][int(index1)+1])
                        self.addEdge(vertexAddress[i], vertexAddress[j], weight)
                        
                    vertexIndex[i] = None
                    
                    
    def addEdge(self, u, v, weight):
        if u in self.vertices and v in self.vertices:
            self.edges[self.edgeIndices[u]][self.edgeIndices[v]] = weight
            self.edges[self.edgeIndices[v]][self.edgeIndices[u]] = weight
            return True
        else:
            return False

    def printMatrix(self):
        print("Graph vertices and adjacency matrix:")
        for vertex in self.edgeIndices.items():
            print(f"Vertex: {vertex}")
        print("\nAdjacency matrix:")
        for row in self.edges:
            print(' '.join(map(str, row)))

                
            
        

        
        

        
