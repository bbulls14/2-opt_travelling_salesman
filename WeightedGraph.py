import csv

class Vertex:
    def __init__(self, n):
        self.name = n

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []
        self.edgeIndices = {}
        self.vertexData = []
        self.distances = []
        self.load_data('WGUPS Addresses.csv', 'WGUPS Distances.csv')
        self.initialize_vertices_and_edges()

    def getDistanceData(self, distanceFile):
        distances = []
        with open(distanceFile, mode='r', encoding='UTF-8-sig') as file:
            csvFile = csv.reader(file, delimiter=',')
            for row in csvFile:
                distanceRow = []
                for j, value in enumerate(row):
                    if value:
                        weight = float(value)
                    else:
                        weight = 0.0  
                    distanceRow.append(weight)
                distances.append(distanceRow)
        return distances

    def load_data(self, vertex_file, distance_file):
        with open(vertex_file, mode='r', encoding='UTF-8-sig') as file:
            csvFile = csv.reader(file, delimiter=',')
            for row in csvFile:
                vertex = row[0]  # Assuming the first column is the vertex name
                self.vertexData.append(Vertex(vertex))

        self.distances = self.getDistanceData(distance_file)

    def initialize_vertices_and_edges(self):
        for vertex in self.vertexData:
            self.addVertex(vertex)

        for i, row in enumerate(self.distances):
            for j, weight in enumerate(row):
                if weight != 0.0:  # Assuming '0.0' indicates no direct edge
                    self.addEdge(self.vertexData[i].name, self.vertexData[j].name, weight)

    def addVertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            
            # Update edges matrix for the new vertex
            for row in self.edges:
                row.append(0.0)
            self.edges.append([0.0] * (len(self.edges) + 1))
            
            # Update edge indices
            self.edgeIndices[vertex.name] = len(self.edgeIndices)
            
            return True
        else:
            return False

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



# Example usage



# # Example usage:
# g = Graph()
# g.printGraph()
          
        
    
        
        
    
             
            
        
    


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
                
            
        

        
        

        
