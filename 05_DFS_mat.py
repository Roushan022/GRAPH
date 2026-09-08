class Graph:
    def __init__(self,vertex):
        self.mat=[[0]*vertex for _ in range(vertex)]
        self.size=vertex
    def add_edge(self,src,dest):
        if (0<= src < self.size and 0 <= dest < self.size):
            self.mat[src][dest]=1
        else:
            print("Invalid ")
    def dfs(self,src):
        visited=[False]*self.size
        stack=[src]
        while(stack):
            v=stack.pop()
            if (visited[v]==False):
                print(v,end=" ")
                visited[v]=True

            for i in range(self.size):
                if self.mat[v][i]==1 and visited[i]==False:
                    stack.append(i)

G=Graph(6)
G.add_edge(0,1)
G.add_edge(0,2)
G.add_edge(2,4)
G.add_edge(2,3)
G.add_edge(3,5)
G.dfs(0)



        
