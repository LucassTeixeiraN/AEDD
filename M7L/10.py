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
        
    def add_edge(self,source,destination, weight):
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
            self.__g[indexS][indexD] = weight


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

    def min_path(self, start_vertex):
        if start_vertex not in self.__listofVertex:
            print(f"O vértice {start_vertex} não existe no grafo.")
            return

        start_index = self.__listofVertex.index(start_vertex)
        distances = [float('inf')] * self.__n  # Inicialmente, todas as distâncias são infinitas
        distances[start_index] = 0  # Distância do vértice inicial para si mesmo é 0
        visited = [False] * self.__n  # Nenhum vértice foi visitado no início

        for _ in range(self.__n):
            # Encontrar o vértice não visitado com a menor distância atual
            min_distance = float('inf')
            min_index = -1
            for i in range(self.__n):
                if not visited[i] and distances[i] < min_distance:
                    min_distance = distances[i]
                    min_index = i

            # Marcar o vértice como visitado
            visited[min_index] = True

            # Atualizar as distâncias dos vértices adjacentes
            for j in range(self.__n):
                if self.__g[min_index][j] > 0 and not visited[j]:  # Existe uma aresta
                    new_distance = distances[min_index] + self.__g[min_index][j]
                    if new_distance < distances[j]:
                        distances[j] = new_distance

        # Imprimir os resultados
        print(f"Menores distâncias a partir do vértice {start_vertex}:")
        for i in range(self.__n):
            if distances[i] == float('inf'):
                print(f"Para {self.__listofVertex[i]}: Inalcançável")
            else:
                print(f"Para {self.__listofVertex[i]}: {distances[i]}")


g = GraphAM("A")
g.add_vertex("B", "C")
g.add_vertex("D", "E")
g.add_vertex("F", "G")
g.add_edge("A", "B", 5)
g.add_edge("A", "C", 3)
g.add_edge("B", "G", 1)
g.add_edge("B", "E", 3)
g.add_edge("B", "C", 2)
g.add_edge("C", "E", 7)
g.add_edge("C", "D", 7)
g.add_edge("D", "A", 2)
g.add_edge("D", "F", 6)
g.add_edge("E", "D", 2)
g.add_edge("E", "F", 1)
g.add_edge("G", "E", 1)

g.print_graph()

g.min_path("A")