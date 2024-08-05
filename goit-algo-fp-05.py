from shared import heapify, array_to_tree, Node, draw_tree
from collections import deque

def color_generator():
    r = 0
    g = 0
    b = 0
    while True:
        yield f"#{r:02x}{g:02x}{b:02x}"
        r = (r + 1) % 256
        g = (g + 2) % 256
        b = (b + 3) % 256

def dfs(root):
    stack = [(root, color_generator())]
    while stack:
        node, color = stack.pop()
        if node is not None:
            node.color = next(color)
            stack.append((node.right, color))
            stack.append((node.left, color))

def bfs(root):
    queue = deque([(root, color_generator())])
    while queue:
        node, color = queue.popleft()
        if node is not None:
            node.color = next(color)
            queue.append((node.left, color))
            queue.append((node.right, color))

# побудова бінарного дерева
arr = [4, 10, 3, 5, 1]
heapify(arr, Node)
root = array_to_tree(arr, Node)

# обхід в глибину та візуалізація
dfs(root)
draw_tree(root)

# обхід в ширину та візуалізація
bfs(root)
draw_tree(root)