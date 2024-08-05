# вузел однозвязного списку
class Node:
    def __init__(self, data=None):
        self.data = data  # дані вузла
        self.next = None  # посилання на наступний вузол

# однозвязний списку
class LinkedList:
    def __init__(self):
        self.head = None  # голова списку

    # додавання вузла в кінець списку
    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    # вивод списку
    def display(self):
        elements = []
        cur_node = self.head
        while cur_node:
            elements.append(cur_node.data)
            cur_node = cur_node.next
        return elements

    # реверсуванн списку
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    # сортування списку вставками
    def insertion_sort(self):
        sorted_list = LinkedList()
        current = self.head
        while current is not None:
            next = current.next
            sorted_list.sorted_insert(current)
            current = next
        self.head = sorted_list.head

    # вставки вузла в відсортований список
    def sorted_insert(self, new_node):
        if self.head is None or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

# об'єднання двох відсортованих списків
def merge_sorted_lists(list1, list2):
    merged_list = LinkedList()
    current1 = list1.head
    current2 = list2.head
    while current1 is not None and current2 is not None:
        if current1.data <= current2.data:
            merged_list.append(current1.data)
            current1 = current1.next
        else:
            merged_list.append(current2.data)
            current2 = current2.next
    while current1 is not None:
        merged_list.append(current1.data)
        current1 = current1.next
    while current2 is not None:
        merged_list.append(current2.data)
        current2 = current2.next
    return merged_list

# перевіряємо роботу алгоритмів
list1 = LinkedList()
list2 = LinkedList()
list1.append(5)
list1.append(3)
list1.append(9)
list1.append(1)
list1.append(6)
list2.append(4)
list2.append(2)
list2.append(8)
list2.append(7)
list2.append(0)

print("Початковий список 1:", list1.display())
print("Початковий список 2:", list2.display())

# реверсуємо
list1.reverse()
list2.reverse()

print("Реверсований список 1:", list1.display())
print("Реверсований список 2:", list2.display())

# сортуємо списки
list1.insertion_sort()
list2.insertion_sort()

print("Відсортований список 1:", list1.display())
print("Відсортований список 2:", list2.display())

# об'єднуємо відсортовані списки
merged_list = merge_sorted_lists(list1, list2)

print("Об'єднаний відсортований список:", merged_list.display())