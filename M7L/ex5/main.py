'''Escreva uma versão não recursiva do algoritmo de busca em profundidade.'''
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u: int, v: int):
        self.graph[u].append(v)

    def DFS(self, start_vertex):
        stack = []
        visited = set()

        stack.append(start_vertex)

        while stack:
            current = stack.pop()
            if current not in visited:
                print(current, end=" ")
                visited.add(current)

            for neighbor in reversed(self.graph[current]):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=" ")
        
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)
                
    def DFSRecursive(self, v):
        visited = set()
        self.DFSUtil(v, visited)

def main():
    g = Graph()

    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is Depth First Traversal (starting from vertex 2):")
    g.DFS(2)
    print()
    g.DFSRecursive(2)

if __name__ == "__main__":
    main()
