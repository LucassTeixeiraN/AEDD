class Grafo:
    def __init__(self):
        self.matriz_adj = []
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = len(self.vertices)
        
            for linha in self.matriz_adj:
                linha.append(0)
            self.matriz_adj.append([0] * (len(self.vertices)))
        else:
            print(f"Vértice {vertice} já existe no grafo.")

    def conectar_vertices(self, vertice1, vertice2):
        if vertice1 in self.vertices and vertice2 in self.vertices:
            i = self.vertices[vertice1]
            j = self.vertices[vertice2]
            self.matriz_adj[i][j] = 1
        else:
            print(f"Um ou ambos os vértices {vertice1}, {vertice2} não existem no grafo.")

    def imprimir_matriz_adj(self):
        print("Matriz de Adjacência:")
        for linha in self.matriz_adj:
            print(" ".join(map(str, linha)))

    def obter_vizinhos(self, vertice):
        if vertice in self.vertices:
            i = self.vertices[vertice]
            vizinhos = [v for v, j in self.vertices.items() if self.matriz_adj[i][j] == 1]
            return vizinhos
        else:
            print(f"Vértice {vertice} não existe no grafo.")
            return []
def main():
    grafo = Grafo()
    grafo.adicionar_vertice('A')
    grafo.adicionar_vertice('B')
    grafo.adicionar_vertice('C')
    grafo.conectar_vertices('A', 'B')
    grafo.conectar_vertices('B', 'C')
    grafo.imprimir_matriz_adj()
    print(f"Vizinhos do nó 'A': {grafo.obter_vizinhos('A')}")
    print(f"Vizinhos do nó 'B': {grafo.obter_vizinhos('B')}")
    
main()
