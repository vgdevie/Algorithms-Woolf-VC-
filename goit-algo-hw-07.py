# імпортуємо потрібні бібліотеки
import networkx as nx
import matplotlib.pyplot as plt

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
dfs_paths = list(nx.dfs_edges(G, source='A'))
print(f"DFS шляхи: {dfs_paths}")

# використовуємо BFS для знаходження шляхів
bfs_paths = list(nx.bfs_edges(G, source='A'))
print(f"BFS шляхи: {bfs_paths}")

# додаємо ваги до ребер
for edge in G.edges():
    G[edge[0]][edge[1]]['weight'] = 1

# використовуємо алгоритм Дейкстри для знаходження найкоротшого шляху
for node in G.nodes():
    print(f"Найкоротший шлях від A до {node}: {nx.dijkstra_path(G, 'A', node)}")