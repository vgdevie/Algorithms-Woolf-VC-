# імпортуємо потрібні бібліотеки
import networkx as nx
import matplotlib.pyplot as plt

# BFS
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

# DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

# Алгоритм дейкстри
def dijkstra(graph, start):
    shortest_paths = {start: (None, 0)}
    current_node = start
    visited = set()
    
    while current_node is not None:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.edges[current_node][next_node] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            break
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    return shortest_paths


# створюємо граф
G = nx.Graph()

# додаємо вершини та ребра в граф
edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'A')]
G.add_edges_from(edges)

# візуалізуємо граф
nx.draw(G, with_labels=True)
plt.show()

# аналізуємо граф
print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")

# використовуємо DFS для знаходження шляхів
dfs_paths = dfs(G, 'A')
print(f"DFS шляхи: {dfs_paths}")

# використовуємо BFS для знаходження шляхів
bfs_paths = bfs(G, 'A')
print(f"BFS шляхи: {bfs_paths}")

# додаємо ваги до ребер
for edge in G.edges():
    G[edge[0]][edge[1]]['weight'] = 1

# використовуємо алгоритм Дейкстри для знаходження найкоротшого шляху
for node in G.nodes():
    shortest_paths = dijkstra(G, 'A')
    path = []
    while node is not None:
        path.append(node)
        next_node = shortest_paths[node][0]
        node = next_node
    path = path[::-1]
    print(f"Найкоротший шлях від A до {node}: {path}")