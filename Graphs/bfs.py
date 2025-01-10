class Graph:
    def __init__(self):
        self.graph={}

    def addEdge(self,u,v):
        if u not in self.graph:
            self.graph[u]=[]
        if v not in self.graph:
            self.graph[v]=[]
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")

            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

g = Graph()
g.addEdge(0,4)  
g.addEdge(0,2)
g.addEdge(2,3)
g.addEdge(3,5)
g.addEdge(3,6)
g.addEdge(4,2)

print("Breadth-First Search Starting From Vertex 2: ")

g.bfs(2)
