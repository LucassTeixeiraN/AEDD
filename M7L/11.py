class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matriz_adj = [[0] * num_vertices for _ in range(num_vertices)]
        self.lista_adj = {i: [] for i in range(1, num_vertices + 1)}

    def adicionar_aresta(self, u, v):
      
        self.matriz_adj[u-1][v-1] = 1
        self.matriz_adj[v-1][u-1] = 1 
       
        self.lista_adj[u].append(v)
        self.lista_adj[v].append(u)

    def imprimir_matriz_adj(self):
        print("Matriz de Adjacência:")
        for linha in self.matriz_adj:
            print(" ".join(map(str, linha)))

    def imprimir_lista_adj(self):
        print("\nLista de Adjacência:")
        for vertice in self.lista_adj:
            print(f"{vertice}: {', '.join(map(str, self.lista_adj[vertice]))}")

    def desenhar_grafo(self):
        print("\nDesenho do Grafo:")
        for vertice in self.lista_adj:
            vizinhos = self.lista_adj[vertice]
            for vizinho in vizinhos:
                print(f"{vertice} -- {vizinho}")
def main():
    grafo = Grafo(8)
    arestas = [
        (1, 2), (1, 3), (1, 4),
        (2, 3), (2, 4),
        (3, 4),
        (4, 6),
        (5, 6), (5, 7), (5, 8),
        (6, 7),
        (7, 8)
    ]
    for u, v in arestas:
        grafo.adicionar_aresta(u, v)

    grafo.imprimir_matriz_adj()
    grafo.imprimir_lista_adj()
    grafo.desenhar_grafo()
main()
