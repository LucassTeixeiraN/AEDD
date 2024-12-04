class Grafo:
    def __init__(self, num_vertices):
        # Inicializa o grafo com o número de vértices
        self.num_vertices = num_vertices
        # Lista de adjacência, onde cada vértice tem uma lista de vizinhos
        self.adjacencia = [[] for _ in range(num_vertices)]

    def adicionar_aresta(self, u, v):
        # Adiciona uma aresta entre os vértices u e v
        self.adjacencia[u].append(v)
        self.adjacencia[v].append(u)  # Se for um grafo não direcionado

    def mostrar(self):
        # Mostra a lista de adjacência do grafo
        for i in range(self.num_vertices):
            print(f'{i}: {self.adjacencia[i]}')

    @classmethod
    def ler_arquivo(cls, nome_arquivo):
        # Lê um grafo a partir de um arquivo
        with open(nome_arquivo, 'r') as f:
            num_vertices = int(f.readline().strip())  # Lê o número de vértices
            grafo = cls(num_vertices)
            for linha in f:
                u, v = map(int, linha.strip().split())
                grafo.adicionar_aresta(u, v)
        return grafo
