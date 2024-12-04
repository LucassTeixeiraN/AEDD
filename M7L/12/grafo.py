grafo = {
    'a': ['b', 'f'],
    'b': ['c', 'e'],
    'c': ['d', 'g'],
    'd': [],
    'e': ['f'],
    'f': ['h'],
    'g': ['e', 'h'],
    'h': ['d']
}

# Função de busca em profundidade
def busca_profundidade(grafo, vertice, visitados=None):
    if visitados is None:
        visitados = set()

    # Marca o vértice como visitado
    visitados.add(vertice)
    print(vertice, end=" ")  # Exibe o vértice visitado

    # Explora os vizinhos não visitados
    for vizinho in grafo[vertice]:
        if vizinho not in visitados:
            busca_profundidade(grafo, vizinho, visitados)
