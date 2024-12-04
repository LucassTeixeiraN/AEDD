'''Execute o algoritmo do caminho mínimo para o grafo abaixo e determine o custo do
menor caminho entre os vértices x e t.'''

# Classe para representar o grafo
class Graph:
    def __init__(self):
        self.graph = {}

    # Adiciona uma aresta ao grafo
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = {}
        if v not in self.graph:
            self.graph[v] = {}
        self.graph[u][v] = weight

    # Implementação do algoritmo de Dijkstra
    def dijkstra(self, start, end):
        # Inicializar distâncias e visitados
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        visited = set()
        previous_nodes = {node: None for node in self.graph}

        while len(visited) < len(self.graph):
            # Encontrar o nó não visitado com a menor distância
            current_node = None
            current_distance = float('inf')
            for node in self.graph:
                if node not in visited and distances[node] < current_distance:
                    current_node = node
                    current_distance = distances[node]

            # Parar se não houver mais nós acessíveis
            if current_node is None:
                break

            # Marcar o nó atual como visitado
            visited.add(current_node)

            # Atualizar as distâncias dos vizinhos do nó atual
            for neighbor, weight in self.graph[current_node].items():
                if neighbor not in visited:
                    new_distance = distances[current_node] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous_nodes[neighbor] = current_node

        # Reconstruir o caminho do final ao início
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous_nodes[current]
        path.reverse()

        return distances[end], path

# Função principal
def main():
    # Criando o grafo
    g = Graph()
    g.add_edge('x', 'v', 30)
    g.add_edge('x', 'z', 12)
    g.add_edge('v', 'u', 15)
    g.add_edge('v', 'r', 17)
    g.add_edge('u', 't', 5)
    g.add_edge('z', 'r', 25)
    g.add_edge('z', 's', 20)
    g.add_edge('r', 't', 7)
    g.add_edge('s', 't', 12)

    # Calculando o menor caminho entre 'x' e 't'
    shortest_distance, shortest_path = g.dijkstra('x', 't')
    print(f"Menor distância: {shortest_distance}")
    print(f"Caminho: {' -> '.join(shortest_path)}")

if __name__ == "__main__":
    main()
