'''Dado os grafos abaixo, crie um programa que mostre o resultado da busca em
largura e em profundidade começando do vértice 1.'''

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, start_vertex):
        visited = set()
        stack = [start_vertex]
        result = []

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                result.append(current)

                for neighbor in reversed(self.graph[current]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return result

    def BFS(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        result = []

        while queue:
            current = queue.popleft()
            if current not in visited:
                visited.add(current)
                result.append(current)

                for neighbor in self.graph[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return result

def main():
    graph1 = Graph()
    edges1 = [
        (1, 2), (1, 5),
        (2, 3), (2, 6),
        (3, 4),
        (4, 1),
        (5, 6), (5, 7),
        (6, 8),
        (7, 9)
    ]
    for u, v in edges1:
        graph1.addEdge(u, v)

    graph2 = Graph()
    edges2 = [
        (1, 2), (1, 4),
        (2, 3), (2, 5),
        (3, 6),
        (4, 7),
        (5, 6), (5, 7),
        (6, 8),
        (7, 8)
    ]
    for u, v in edges2:
        graph2.addEdge(u, v)


    print("Grafo 1:")
    print("DFS:", graph1.DFS(1))
    print("BFS:", graph1.BFS(1))

    print("\nGrafo 2:")
    print("DFS:", graph2.DFS(1))
    print("BFS:", graph2.BFS(1))

if __name__ == "__main__":
    main()
