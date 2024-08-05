from shared import heapify, array_to_tree, Node, draw_tree


# візуалізація бінарної купи
def visualize_heap(arr):
    heapify(arr, Node)
    root = array_to_tree(arr, Node)
    draw_tree(root)

# пробуємо
visualize_heap([4, 10, 3, 5, 1])