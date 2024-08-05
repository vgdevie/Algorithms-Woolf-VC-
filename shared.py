import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
  def __init__(self, key, color="skyblue"):
    self.left = None
    self.right = None
    self.val = key
    self.color = color # Додатковий аргумент для зберігання кольору вузла
    self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
  if node is not None:
    graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
    if node.left:
      graph.add_edge(node.id, node.left.id)
      l = x - 1 / 2 ** layer
      pos[node.left.id] = (l, y - 1)
      l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
    if node.right:
      graph.add_edge(node.id, node.right.id)
      r = x + 1 / 2 ** layer
      pos[node.right.id] = (r, y - 1)
      r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
  return graph


def draw_tree(tree_root):
  tree = nx.DiGraph()
  pos = {tree_root.id: (0, 0)}
  tree = add_edges(tree, tree_root, pos)

  colors = [node[1]['color'] for node in tree.nodes(data=True)]
  labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

  plt.figure(figsize=(8, 5))
  nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
  plt.show()

# функція для перетворення масиву в бінарну купу
def build_heap(arr, n, i, Node):
    largest = i 
    l = 2 * i + 1     # лівий = 2*i + 1
    r = 2 * i + 2     # правий = 2*i + 2

    # чи існує лівий дочірній елемент більший, ніж корінь
    if l < n and arr[i] < arr[l]:
        largest = l

    # чи існує правий дочірній елемент більший, ніж корінь
    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # своп

        # Рекурсивно перетворюємо змінене піддерево
        build_heap(arr, n, largest, Node)

# перетворення масиву на бінарну купу
def heapify(arr, Node):
    n = len(arr)

    for i in range(n, -1, -1):
        build_heap(arr, n, i, Node)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        build_heap(arr, i, 0, Node)

# перетворення масиву в дерево
def array_to_tree(arr, Node):
    n = len(arr)
    nodes = [None]*n
    for i in range(n):
        nodes[i] = Node(arr[i])
    for i in range(n//2 - 1, -1, -1):
        if 2*i + 1 < n:
            nodes[i].left = nodes[2*i + 1]
        if 2*i + 2 < n:
            nodes[i].right = nodes[2*i + 2]
    return nodes[0] if nodes else None