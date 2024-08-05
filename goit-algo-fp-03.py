import heapq

# створення графа
def create_graph(num_vertices):
    graph = {vertex: {} for vertex in range(num_vertices)}
    return graph

# додавання ребра до  графа
def add_edge(graph, from_vertex, to_vertex, weight):
    graph[from_vertex][to_vertex] = weight
    graph[to_vertex][from_vertex] = weight

# алгоритм дейкстри
def deikstra(graph, start_vertex):
    
    # ініціалізація відстаней та черги пріоритетів
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0
    queue = [(0, start_vertex)]

    while queue:
        # вибираємо вершину з найменшою відстанню
        current_distance, current_vertex = heapq.heappop(queue)

        # перевіряємо чи не була вже оброблена ця вершина
        if current_distance == distances[current_vertex]:
            for neighbor, weight in graph[current_vertex].items():
                # розраховуємо нову відстань до сусідньої вершини
                new_distance = current_distance + weight

                # якщо нова відстань менша, то оновлюємо її
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(queue, (new_distance, neighbor))

    return distances

# створюємо граф
graph = create_graph(5)

add_edge(graph, 0, 1, 1)
add_edge(graph, 0, 2, 3)
add_edge(graph, 1, 2, 1)
add_edge(graph, 1, 3, 7)
add_edge(graph, 2, 4, 1)
add_edge(graph, 3, 4, 1)

distances = deikstra(graph, 0)

print(distances)