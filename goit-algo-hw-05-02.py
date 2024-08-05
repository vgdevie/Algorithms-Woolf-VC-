def binary_search(arr, x):
    # встановлюємо початкові значення для нижньої, верхньої межі та лічильника ітерацій
    low = 0
    high = len(arr) - 1
    iterations = 0

    # виконуємо пошук, поки нижня межа не перевищить верхню
    while low <= high:
        # збільшуємо лічильник ітерацій
        iterations += 1
        # визначаємо середину масиву
        mid = (high + low) // 2

        # якщо знайдений елемент менший, ніж шуканий, то шукаємо в правій половині
        if arr[mid] < x:
            low = mid + 1
        # якщо знайдений елемент більший, ніж шуканий, то шукаємо в лівій половині
        elif arr[mid] > x:
            high = mid - 1
        # якщо елемент знайдено, повертаємо кількість ітерацій та елемент
        else:
            return iterations, arr[mid]

    # якщо елемент не знайдено, повертаємо кількість ітерацій та найменший елемент, який більший за шуканий
    return iterations, arr[low] if low < len(arr) else None