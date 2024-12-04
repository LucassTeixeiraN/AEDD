# Representação do grafo como dicionário de adjacência
class ArvoreDFS:
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

    # Busca em Profundidade (DFS) para construir a árvore geradora
    def dfs_tree(start, grafo):
        visitados = set()
        arvore = []

        def dfs(no):
            visitados.add(no)
            for vizinho in sorted(grafo[no]):  # Ordem alfabética
                if vizinho not in visitados:
                    arvore.append((no, vizinho))
                    dfs(vizinho)

        dfs(start)
        return arvore
