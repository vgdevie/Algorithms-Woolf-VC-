import heapq

# функція для об'єднання кабелів
def connect_cables(cables):

    heapq.heapify(cables)
    total_cost = 0

    # поки в купі є більше ніж один кабель
    while len(cables) > 1:
        # видаляємо два найменші кабелі
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)
        
        total_cost += cable1 + cable2
        
        heapq.heappush(cables, cable1 + cable2)
    
    return total_cost

# функція длч об'єднання відсортованих списків
def merge_k_lists(lists):


    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    merged_list = []

    # поки в купі є елементи
    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)
        
        merged_list.append(val)
        
        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1], list_ind, element_ind + 1)
            heapq.heappush(heap, next_tuple)
    
    return merged_list

cables = [5, 4, 2, 8]
cost = connect_cables(cables)
print("Загальні витрати:", cost)

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)