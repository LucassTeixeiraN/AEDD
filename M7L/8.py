
graph = {
    'A': {'B': 15, 'C': 10, 'D': 19},
    'B': {'A': 15, 'C': 7, 'D': 17},
    'C': {'A': 10, 'B': 7, 'D': 16, 'E': 14},
    'D': {'A': 19, 'B': 17, 'C': 16, 'E': 12, 'F': 6, 'G': 3},
    'E': {'C': 14, 'D': 12, 'F': 20, 'G': 13},
    'F': {'D': 6, 'E': 20, 'G': 9, 'H': 5},
    'G': {'D': 3, 'E': 13, 'F': 9, 'H': 20, 'I': 4, 'J': 11},
    'H': {'F': 5, 'G': 20, 'I': 2},
    'I': {'G': 4, 'H': 2, 'J': 18},
    'J': {'G': 11, 'I': 18}
}

def prims_algorithm(graph, start):
    mst = []
    visited = set([start])
    edges = []

    for neighbor, weight in graph[start].items():
        edges.append((weight, start, neighbor))
    
    while edges:
     
        edges.sort()
        weight, frm, to = edges.pop(0)

        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))

            for next_to, weight in graph[to].items():
                if next_to not in visited:
                    edges.append((weight, to, next_to))
                    
    return mst
def main():
    mst = prims_algorithm(graph, 'A')

    print("Árvore Geradora Mínima (MST):")
    for edge in mst:
        print(f"{edge[0]} - {edge[1]}: {edge[2]}")
main()
