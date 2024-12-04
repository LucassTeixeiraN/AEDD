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

    def eh_aciclico(self):
        visitados = set()
        rec_stack = set()

        def dfs(vertice, parent):
            visitados.add(vertice)
            rec_stack.add(vertice)
            for vizinho in self.obter_vizinhos(vertice):
                if vizinho not in visitados:
                    if dfs(vizinho, vertice):
                        return True
                elif vizinho != parent and vizinho in rec_stack:
                    return True
            rec_stack.remove(vertice)
            return False

        for vertice in self.adjacencia:
            if vertice not in visitados:
                if dfs(vertice, None):
                    return False
        return True

def main():
    grafo = Grafo()


    N = 5  
    for i in range(N):
        grafo.adicionar_vertice(f"V{i}")

    grafo.conectar_vertices("V0", "V1")
    grafo.conectar_vertices("V0", "V2")
    grafo.conectar_vertices("V1", "V3")
    grafo.conectar_vertices("V1", "V4")
    # grafo.conectar_vertices("V3", "V0")  # 


    if grafo.eh_aciclico():
        print("O grafo é acíclico.")
    else:
        print("O grafo contém ciclos.")


    grafo.imprimir_lista_adjacencia()

main()
