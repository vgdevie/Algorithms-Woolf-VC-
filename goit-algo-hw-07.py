class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Завдання 1 - функція для пошуку максимального значення в дереві
def find_max(node):

    if node is None:
        return None

    # переходимо до крайнього правого вузла
    while node.right is not None:
        node = node.right

    # повертаємо значення крайнього правого вузла
    return node.val

# Завдання 2 - функція для пошуку мінімального значення в дереві
def find_min(node):

    if node is None:
        return None

    # переходимо до крайнього лівого вузла
    while node.left is not None:
        node = node.left

    # повертаємо значення крайнього лівого вузла
    return node.val

# Завдання 3 - функція для пошуку суми всіх значень в дереві
def find_sum(node):

    if node is None:
        return 0

    # сума значення поточного вузла та суми значень лівого та правого піддерев
    return node.val + find_sum(node.left) + find_sum(node.right)

# створюємо дерево
root = Node(20)
root.left = Node(10)
root.right = Node(30)
root.left.left = Node(5)
root.left.right = Node(15)
root.right.left = Node(25)
root.right.right = Node(35)

print("Найбільше значення в дереві:", find_max(root))
print("Найменше значення в дереві:", find_min(root))
print("Сума всіх значень в дереві:", find_sum(root))