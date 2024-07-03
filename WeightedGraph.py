import csv

class Vertex:
    def __init__(self, n):
        self.name = n
        
class Graph:
    vertices = {}
    edges = []
    edge_indices = { }
    
        
    def addVertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0] * (len(self.edges)+1))
            self.edge_indices[vertex.name] = len(self.edge_indices)
            return True
        else:
            return False
    
       
    def addEdge(self, u, v, weight):
        
        if u in self.vertices and v in self.vertices:
            self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
            self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
            return True
        else:
            return False
    
    def printGraph(self):
        for v, i in self.edge_indices.items():
            
            print(v + ' ', end='')
            for j in range(len(self.edges)):
                print(self.edges[i][j], end='')
            print(' ')






# class Edge:
#     def __init__(self):
#         self.sourceVertex = None
#         self.destinationVertex = None
#         self.distance = None
#     def makeEdges(self, data):
#         self.Edge = ()
        
# def makeGraph(data):
#     graph = {}
#     sourceVertex = []
#     Edge.edge = ()
#     for i in range(7, len(data)):
#         sourceVertex = data.iloc[i,0]
#         graph[sourceVertex] = {}
        
        
            
            
        
    
        
        
    
             
            
        
    


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
                
            
        

        
        

        
