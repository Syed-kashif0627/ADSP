class Graph:
    def __init__(self):
        self.graph={}
    
    def addEdge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        self.graph[u].append(v)
    
    def dfs(self,start):
        visited=set()
        stack=[start]

        while stack:
            vertex=stack.pop()
            if vertex not in visited:
                print(vertex, end=" ")
                visited.add(vertex)
                for neighbor in reversed(self.graph.get(vertex,[])):
                    if neighbor not in visited:
                        stack.append(neighbor)


g=Graph()
g.addEdge(0,4)
g.addEdge(0,2)
g.addEdge(4,4)
g.addEdge(4,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

print("Depth-First Search Starting From Vertex 4: ")

g.dfs(4)