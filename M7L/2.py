'''2. Crie um programa capaz de:
a. Instanciar um novo grafo.
b. Adicionar um vértice ao grafo.
c. Conectar dois vértices.
d. Imprimir o grafo em forma de Matriz de Adjacências.
e. Obter todos os nós adjacentes (vizinhos) a um nó do grafo (usando a MA).'''

class GraphAM:
    __n = 0
    __g = [[0 for column in range(10)] for row in range(10)]
    __listofVertex = []

    def __init__(self, vertex):
        self.__listofVertex.append(vertex)
        self.__n = len(self.__listofVertex)
        for source in range(0, self.__n):
            for destination in range(0, self.__n):
                self.__g[source][destination] = 0

    def add_vertex(self, source, destination):
        indexS = 0
        indexD = 0
        if source in self.__listofVertex:
            indexS=self.__listofVertex.index(source)
        else:
            print(f"Vertex {source} not present in Graph, adding it automatically")
            self.__listofVertex.append(source)
            indexS=self.__listofVertex.index(source)
            self.__n = self.__n + 1
        
        if destination in self.__listofVertex:
            indexD = self.__listofVertex.index(destination)
        else:
            print(f"Vertex {destination} not present in Graph, adding it automatically")
            self.__listofVertex.append(destination)
            indexD=self.__listofVertex.index(destination)
            self.__n = self.__n + 1

        if (indexS >= self.__n) or (indexD >= self.__n):
            print("One of the vertex doesn't exists!")

        if self.__n > 1:
            for i in range(0, self.__n):
                self.__g[i][self.__n-1] = 0
                self.__g[self.__n-1][i] = 0
        
    def add_edge(self,source,destination):
        indexS=0
        indexD=0
        if source in self.__listofVertex:
            indexS=self.__listofVertex.index(source)
        else:
            print("Cannot be included in the graph, Add the vertex {O}".format(source))

        if destination in self.__listofVertex:
            indexD=self.__listofVertex.index(destination)
        else:
            print(f"Cannot be included in graph, add the vertex {destination}")
        
        if indexS > 0 and indexS == indexD:
            print("Same Source and Destination")
        else:
            self.__g[indexS][indexD] = 1
            self.__g[indexD][indexS] = 1

    def removeVertex(self, location):
        indexL=0
        if location in self.__listofVertex:
            indexL = self.__listofVertex.index(location)
            while indexL < self.__n :
                for i in range(0, self.__n):
                    self.__g[i][indexL] = self.__g[i][indexL + 1]

                for i in range(0, self.__n):
                    self.__g[indexL][i] = self.__g[indexL + 1][i]
                indexL = indexL + 1

            self.__n = self.__n - 1
            print(f"Successfully removed {location} from graph,current list Of vertex are below:\n{self.__listofVertex}")
        else:
            print("No such vertex exist in the graph")                

    def print_graph(self):
        print("\n")
        for i in range(len(self.__listofVertex)):
            print("\t", self.__listofVertex[i], end = "")
        for i in range(0, self.__n):
            print("\n", self.__listofVertex[i], end=" ")
            for j in range(0, self.__n):
                print("\t", self.__g[i][j], end="")
        print("\n")

    def print_adjacent(self, node):

        if node not in self.__listofVertex:
            print(f"O nó {node} não existe no grafo.")
            return

        index = self.__listofVertex.index(node)
        adjacent_nodes = []

        # Iterar sobre a linha correspondente na matriz de adjacência
        for i in range(self.__n):
            if self.__g[index][i] == 1:  # Verificar se há uma conexão
                adjacent_nodes.append(self.__listofVertex[i])

        if adjacent_nodes:
            print(f"Nós adjacentes ao nó {node}: {', '.join(adjacent_nodes)}")
        else:
            print(f"O nó {node} não tem nós adjacentes.")


g = GraphAM("A")
g.add_vertex("B", "C")
g.add_edge("A", "B")
g.add_edge("B", "C")
g.add_edge("A", "C")

g.print_graph()

# Imprimir nós adjacentes
g.print_adjacent("A")  # Deve listar "B, C"
g.print_adjacent("B")  # Deve listar "A, C"
g.print_adjacent("D")  # Deve informar que o nó não existe