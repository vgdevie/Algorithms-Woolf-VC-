import random
import timeit

# алгоритм сортування вставками
def insertion_sort(arr):
    # проходимо через всі елементи масиву
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        # переміщуємо елементи arr[0..i-1], що більше за key,
        # на одну позицію вперед
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

# алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) >1:
        mid = len(arr)//2 # знаходимо середину масиву
        L = arr[:mid] # ділимо елементи масиву
        R = arr[mid:] # на дві половини

        merge_sort(L) # сортуємо першу половину
        merge_sort(R) # сортуємо другу половину

        i = j = k = 0

        # копіюємо дані в тимчасові масиви L[] та R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i+= 1
            else:
                arr[k] = R[j]
                j+= 1
            k+= 1

        # перевіряємо, чи залишились елементи
        while i < len(L):
            arr[k] = L[i]
            i+= 1
            k+= 1

        while j < len(R):
            arr[k] = R[j]
            j+= 1
            k+= 1

# генеруємо випадковий масив
arr = [random.randint(0, 100) for _ in range(1000)]

# вимірюємо час виконання алгоритмів
start_time = timeit.default_timer()
insertion_sort(arr)
print("Сортування вставкою: ", timeit.default_timer() - start_time)

start_time = timeit.default_timer()
merge_sort(arr)
print("Сортування злиттям: ", timeit.default_timer() - start_time)

start_time = timeit.default_timer()
sorted(arr)
print("Timsort: ", timeit.default_timer() - start_time)

# висновок тімсорт працює швидше за інші алгоритми сортування, вручну їх писати немає сенсу