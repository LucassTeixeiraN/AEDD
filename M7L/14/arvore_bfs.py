from collections import deque
class ArvoreBFS:
    # Representação do grafo como dicionário de adjacência
    grafo = {
        'a': ['b', 'e'],
        'b': ['a', 'c', 'f'],
        'c': ['b', 'd', 'g'],
        'd': ['c', 'h'],
        'e': ['a', 'f', 'i'],
        'f': ['b', 'e', 'g', 'j'],
        'g': ['c', 'f', 'h', 'k'],
        'h': ['d', 'g', 'l'],
        'i': ['e', 'j'],
        'j': ['f', 'i', 'k'],
        'k': ['g', 'j', 'l'],
        'l': ['h', 'k']
    }

    # Busca em Largura (BFS) para construir a árvore geradora
    def bfs_tree(start, grafo):
        visitados = set()
        arvore = []
        fila = deque([start])

        while fila:
            no = fila.popleft()
            if no not in visitados:
                visitados.add(no)
                # Adicionar arestas à árvore
                for vizinho in sorted(grafo[no]):  # Ordem alfabética
                    if vizinho not in visitados:
                        arvore.append((no, vizinho))
                        fila.append(vizinho)
        return arvore

