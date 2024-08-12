from shared import add_edges, array_to_tree, Node
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

# генеруємо колір в форматі RGB
def generate_color(n, max_n):
    r = min(int(255 * ((n + 1) / (max_n + 1))), 255)
    return "#{:02x}{:02x}{:02x}".format(r, 150, 150)

# обхід в глибину з використанням стеку
def dfs(root):
    stack = [(root, 0)]
    max_depth = 0
    while stack:
        node, depth = stack.pop()
        if node:
            node.color = generate_color(depth, max_depth)
            max_depth = max(max_depth, depth)
            stack.append((node.right, depth + 1))
            stack.append((node.left, depth + 1))

# обхід в ширину з використанням черги
def bfs(root):
    queue = [(root, 0)]
    max_level = 0
    while queue:
        node, level = queue.pop(0)
        if node:
            node.color = generate_color(level, max_level)
            max_level = max(max_level, level)
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))

# візуалізація дерева з кольоровими вузлами
def draw_colorful_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(15, 8))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

arr = list(range(1, 100))
root = array_to_tree(arr, Node)
dfs(root)
draw_colorful_tree(root)