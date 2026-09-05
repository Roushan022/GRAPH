class Graph:
    def __init__(self,vertex):
        self.mat=[[0]*vertex for x in range(vertex)]
        self.size=vertex
    
    def add_edge(self,src,dest):
        if (0<= src<self.size and 0 <= dest<self.size):
            self.mat[src][dest]=1
            self.mat[dest][src]=1
        else:
            print("Invalid vertex")
    
    def Print(self):
        for row in self.mat:
            print(" ".join(map(str,row)))
            
G=Graph(4)
G.add_edge(0,1)
G.add_edge(0,3)
G.add_edge(0,2)
G.add_edge(1,3)
G.add_edge(1,2)
G.Print()
