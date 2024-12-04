class Grafo:
    def __init__(self):
        self.arestas = {}
        self.vertices = set()

    def adicionar_aresta(self, origem, destino, peso):
        if origem not in self.arestas:
            self.arestas[origem] = []
        self.arestas[origem].append((destino, peso))
        self.vertices.add(origem)
        self.vertices.add(destino)

    def dijkstra(self, inicio):
        distancias = {vertice: float('inf') for vertice in self.vertices}
        distancias[inicio] = 0
        visitados = set()

        while len(visitados) < len(self.vertices):
            vertice_atual = None
            for vertice in self.vertices:
                if vertice not in visitados:
                    if vertice_atual is None or distancias[vertice] < distancias[vertice_atual]:
                        vertice_atual = vertice

            if distancias[vertice_atual] == float('inf'):
                break

            visitados.add(vertice_atual)
            for vizinho, peso in self.arestas.get(vertice_atual, []):
                nova_distancia = distancias[vertice_atual] + peso
                if nova_distancia < distancias[vizinho]:
                    distancias[vizinho] = nova_distancia
        
        return distancias

def main():
    grafo = Grafo()
    arestas = [
        ('A', 'B', 5), ('A', 'C', 3), ('A', 'D', 2),
        ('B', 'C', 2), ('B', 'G', 1), ('C', 'E', 7),
        ('C', 'F', 2), ('D', 'C', 7), ('D', 'F', 6),
        ('E', 'G', 1), ('F', 'E', 1)
    ]

    for origem, destino, peso in arestas:
        grafo.adicionar_aresta(origem, destino, peso)


    distancias_b = grafo.dijkstra('B')
    print("Caminhos de custo mínimo a partir de B:")
    for vertice, distancia in distancias_b.items():
        print(f"B -> {vertice}: {distancia}")
main()
