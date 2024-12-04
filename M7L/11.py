'''11. Seja um grafo G cujos vértices são os inteiros de 1 a 8 e os vértices adjacentes a
cada vértice são dados pela tabela abaixo:
a. Desenhe o grafo G.
b. Crie um programa que o represente por meio de uma matriz de adjacência e por
meio de uma lista de adjacência.'''

class GraphAM:
    __n = 0
    __g = [[0 for column in range(10)] for row in range(10)]
    __listofVertex = []

    def __init__(self):
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
            self.__listofVertex.append(source)
            indexS=self.__listofVertex.index(source)
            self.__n = self.__n + 1
        
        if destination in self.__listofVertex:
            indexD = self.__listofVertex.index(destination)
        else:
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

    def print_graph(self):
        print("\n")
        for i in range(len(self.__listofVertex)):
            print("\t", self.__listofVertex[i], end = "")
        for i in range(0, self.__n):
            print("\n", self.__listofVertex[i], end=" ")
            for j in range(0, self.__n):
                print("\t", self.__g[i][j], end="")
        print("\n")

class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None

class GraphAL:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    def add_edge(self, s, d):       
        node = AdjNode(d)
        node.next = self.graph[s - 1]
        self.graph[s - 1] =  node
        node = AdjNode(s)
        node.next = self.graph[d - 1]
        self.graph[d - 1] = node

    def print_graph(self):
        for i in range(self.V):
            print(str(i + 1), end='')
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

gAM = GraphAM()
gAL = GraphAL(8)

gAM.add_vertex(1, 2)
gAM.add_vertex(3, 4)
gAM.add_vertex(5, 6)
gAM.add_vertex(7, 8)
gAM.add_edge(1, 2)
gAM.add_edge(1, 3)
gAM.add_edge(1, 4)
gAM.add_edge(2, 3)
gAM.add_edge(2, 4)
gAM.add_edge(3, 4)
gAM.add_edge(4, 6)
gAM.add_edge(5, 6)
gAM.add_edge(5, 7)
gAM.add_edge(5, 8)
gAM.add_edge(6, 7)
gAM.add_edge(7, 8)
gAM.print_graph()

print("-"*70)

gAL.add_edge(1, 2)
gAL.add_edge(1, 3)
gAL.add_edge(1, 4)
gAL.add_edge(2, 3)
gAL.add_edge(2, 4)
gAL.add_edge(3, 4)
gAL.add_edge(4, 6)
gAL.add_edge(5, 6)
gAL.add_edge(5, 7)
gAL.add_edge(5, 8)
gAL.add_edge(6, 7)
gAL.add_edge(7, 8)
gAL.print_graph()