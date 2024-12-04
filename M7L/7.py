class Grafo:
    def __init__(self):
        self.adjacencia = {}
        self.arestas = []

    def adicionar_vertice(self, vertice):
        if vertice not in self.adjacencia:
            self.adjacencia[vertice] = []

    def conectar_vertices(self, vertice1, vertice2, peso):
        if vertice1 in self.adjacencia and vertice2 in self.adjacencia:
            self.adjacencia[vertice1].append((vertice2, peso))
            self.adjacencia[vertice2].append((vertice1, peso))
            self.arestas.append((peso, vertice1, vertice2))

    def imprimir_lista_adjacencia(self):
        for vertice in self.adjacencia:
            print(f"{vertice}: {self.adjacencia[vertice]}")

    def encontrar(self, parent, i):
        if parent[i] == i:
            return i
        else:
            return self.encontrar(parent, parent[i])

    def unir(self, parent, rank, x, y):
        raiz_x = self.encontrar(parent, x)
        raiz_y = self.encontrar(parent, y)
        if rank[raiz_x] < rank[raiz_y]:
            parent[raiz_x] = raiz_y
        elif rank[raiz_x] > rank[raiz_y]:
            parent[raiz_y] = raiz_x
        else:
            parent[raiz_y] = raiz_x
            rank[raiz_x] += 1

    def kruskal(self):
        resultado = []
        i, e = 0, 0
        self.arestas = sorted(self.arestas, key=lambda item: item[0])
        parent = {}
        rank = {}

        for vertice in self.adjacencia:
            parent[vertice] = vertice
            rank[vertice] = 0

        while e < len(self.adjacencia) - 1:
            peso, u, v = self.arestas[i]
            i += 1
            x = self.encontrar(parent, u)
            y = self.encontrar(parent, v)
            if x != y:
                e += 1
                resultado.append((u, v, peso))
                self.unir(parent, rank, x, y)
        
        print("Árvore Geradora Mínima usando Kruskal:")
        for u, v, peso in resultado:
            print(f"{u} -- {v} == {peso}")

    def prim(self, inicio):
        visitados = set([inicio])
        borda = [(inicio, v, peso) for v, peso in self.adjacencia[inicio]]
        mst = []

        while borda:
            menor_peso = float('inf')
            for u, v, peso in borda:
                if peso < menor_peso:
                    menor_peso = peso
                    menor_aresta = (u, v, peso)

            u, v, peso = menor_aresta
            borda.remove(menor_aresta)
            if v not in visitados:
                visitados.add(v)
                mst.append((u, v, peso))
                for proximo_v, proximo_peso in self.adjacencia[v]:
                    if proximo_v not in visitados:
                        borda.append((v, proximo_v, proximo_peso))

        print("Árvore Geradora Mínima usando Prim:")
        for u, v, peso in mst:
            print(f"{u} -- {v} == {peso}")

def menu():
    grafo = Grafo()

    vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for vertice in vertices:
        grafo.adicionar_vertice(vertice)

    arestas = [
        ('a', 'b', 4), ('a', 'h', 11),
        ('b', 'c', 8), ('b', 'h', 7),
        ('c', 'd', 7), ('c', 'f', 4),
        ('c', 'g', 6), ('d', 'e', 9),
        ('d', 'f', 14), ('e', 'f', 10),
        ('f', 'g', 2), ('g', 'h', 6)
    ]
    for aresta in arestas:
        grafo.conectar_vertices(*aresta)

    while True:
        print("\nMenu:")
        print("1. Imprimir lista de adjacência")
        print("2. Encontrar árvore geradora mínima usando Kruskal")
        print("3. Encontrar árvore geradora mínima usando Prim")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            grafo.imprimir_lista_adjacencia()
        elif escolha == '2':
            grafo.kruskal()
        elif escolha == '3':
            inicio = input("Digite o vértice inicial para o algoritmo de Prim: ")
            grafo.prim(inicio)
        elif escolha == '4':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
