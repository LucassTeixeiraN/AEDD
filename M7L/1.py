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

    def findPaths(self, source, destination, length=None):
        if source not in self.__listofVertex or destination not in self.__listofVertex:
            print(f"Um ou ambos os nós {source}, {destination} não existem no grafo.")
            return 0
        
        indexS = self.__listofVertex.index(source)
        indexD = self.__listofVertex.index(destination)
        
        # Para contar os caminhos
        visited = [False] * self.__n
        count = [0]  # Usar uma lista para passar por referência
        
        # Chamar a função auxiliar
        self.findPathsUtil(indexS, indexD, length, visited, count, 0)
        return count[0]

    def findPathsUtil(self, current, destination, max_length, visited, count, path_length):
        # Marcar o nó atual como visitado
        visited[current] = True
        
        # Caso base: Se o nó atual é o destino e o comprimento é apropriado
        if current == destination:
            if max_length is None or path_length == max_length:
                count[0] += 1
        else:
            # Recursão para todos os vértices adjacentes
            for i in range(self.__n):
                if self.__g[current][i] == 1 and not visited[i]:
                    self.findPathsUtil(i, destination, max_length, visited, count, path_length + 1)

        # Desfazer a marcação para permitir outras explorações
        visited[current] = False

g1 = GraphAM("A")
g1.add_vertex("A","B")
g1.add_vertex("B","C")
g1.add_vertex("D","E")
g1.add_edge("A", "B")
g1.add_edge("B", "C")
# g1.add_edge("A", "D")
# g1.add_edge("D", "C")
g1.print_graph()

# Caminhos de comprimento 2 de A para C
print("Caminhos de comprimento 2 de A para C:", g1.findPaths("A", "C", 2))

# Total de caminhos de A para C
print("Total de caminhos de A para C:", g1.findPaths("A", "C"))