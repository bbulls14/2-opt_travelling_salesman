# from datetime import datetime
# from AdjMatrix import Matrix
# from Clock import Clock
# from datetime import datetime, timedelta


    
    
    
    
    # def bestPath(self):
    #     tour = list(self.edgeIndices.values())
    #     n = len(tour)
    #     tourEdges = [(tour[i-1], tour[i]) for i in range (n)]
    #     edgeDistances = [self.edges[tour[i - 1]][tour[i]] for i in range(n)]
        

    #     improved = True
    #     while improved:
    #         improved = False
                
    #         for i in range (n):
    #             for j in range (i+1,n):
    #                 cur1 = (tour[i], tour[i+1])
    #                 cur2 = (tour[j], tour[(j+1)%n])
    #                 curLength = self.edges[i][i+1] + self.edges[j][(j+1)%n]
                    
    #                 new1 = (tour[i], tour[j])
    #                 new2 = (tour[i+1], tour[(j+1)%n])
    #                 newLength = self.edges[i][j] + self.edges[i+1][(j+1)%n]
                    
    #                 if newLength < curLength:
                        
    #                     tour[i+1:j+1] = tour[i+1:j+1][::-1]
    #                     tourEdges = [(tour[i-1], tour[i]) for i in range (n)]
    #                     edgeDistances = [self.edges[tour[i - 1]][tour[i]] for i in range(n)] 
                           
        # tourEdgesWithDistances = dict(zip(tourEdges,edgeDistances))
        # orderedDistances = self.orderedEdgesAndDistances(tourEdges, tourEdgesWithDistances)
        # addressPath = self.addressesFromTour(tour)
        # return addressPath, orderedDistances