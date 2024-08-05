def greedy_algorithm(items, budget):
    # сортуємо страви за співвідношенням калорій до вартості в порядку спадання
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    result = []
    for item in sorted_items:
        # якщо страва вписується в бюджет, додаємо її до результату
        if item[1]['cost'] <= budget:
            result.append(item[0])
            budget -= item[1]['cost']
    
    return result

def dynamic_programming(items, budget):
    # ініціалізуємо двомірний масив
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]
    
    items_list = list(items.items())
    
    for i in range(1, len(items) + 1):
        for w in range(1, budget + 1):
            # якщо страва вписується в бюджет, обчислюємо максимальну калорійність
            if items_list[i - 1][1]['cost'] <= w:
                dp[i][w] = max(dp[i - 1][w], items_list[i - 1][1]['calories'] + dp[i - 1][w - items_list[i - 1][1]['cost']])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # знаходимо оптимальний набір страв
    result = []
    w = budget
    for i in range(len(items), 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            result.append(items_list[i - 1][0])
            w -= items_list[i - 1][1]['cost']
    
    return result

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100  # заданий бюджет

greedy_result = greedy_algorithm(items, budget)
print("Результат жадібного алгоритму:", greedy_result)

dp_result = dynamic_programming(items, budget)
print("Результат алгоритму динамічного програмування:", dp_result)