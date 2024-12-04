class Grafo:
    def __init__(self):
        self.adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.adjacencia:
            self.adjacencia[vertice] = []

    def conectar_vertices(self, vertice1, vertice2):
        if vertice1 in self.adjacencia and vertice2 in self.adjacencia:
            self.adjacencia[vertice1].append(vertice2)
            self.adjacencia[vertice2].append(vertice1)

    def imprimir_lista_adjacencia(self):
        for vertice in self.adjacencia:
            print(f"{vertice}: {self.adjacencia[vertice]}")

    def obter_vizinhos(self, vertice):
        if vertice in self.adjacencia:
            return self.adjacencia[vertice]
        else:
            return []
def main():
    grafo = Grafo()

    N = 5 
    for i in range(N):
        grafo.adicionar_vertice(f"V{i}")


    grafo.conectar_vertices("V0", "V1")
    grafo.conectar_vertices("V0", "V2")
    grafo.conectar_vertices("V1", "V3")
    grafo.conectar_vertices("V1", "V4")

    grafo.imprimir_lista_adjacencia()

    vizinhanca = grafo.obter_vizinhos("V1")
    print(f"Vizinhos de V1: {vizinhanca}")
    
main()
