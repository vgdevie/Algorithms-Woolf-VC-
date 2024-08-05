import timeit

# список доступних монет
coins = [50, 25, 10, 5, 2, 1]

def find_coins_greedy(amount):
    # словник для зберігання результату
    result = {}
    for coin in coins:
        # якщо сума для здачі більша або рівна поточній монеті
        if amount >= coin:
            # визначаємо кількість монет даного номіналу
            num_coins = amount // coin
            # зменшуємо загальну суму на вартість вибраних монет
            amount -= num_coins * coin
            # додаємо вибраний номінал та його кількість до результату
            result[coin] = num_coins
    return result

def find_min_coins(amount):
    # словник для зберігання проміжних результатів
    dp = [0] + [float('inf')] * amount
    # словник для зберігання результату
    result = {}
    for coin in coins:
        for i in range(coin, amount + 1):
            # якщо поточна сума може бути зменшена за допомогою поточної монети
            if dp[i - coin] + 1 < dp[i]:
                # зменшуємо поточну суму
                dp[i] = dp[i - coin] + 1
    # якщо суму неможливо зібрати з наявних монет
    if dp[amount] == float('inf'):
        return None
    # відновлення результату
    while amount > 0:
        for coin in coins:
            # якщо поточна монета була використана при формуванні суми
            if dp[amount - coin] == dp[amount] - 1:
                # додаємо монету до результату
                if coin in result:
                    result[coin] += 1
                else:
                    result[coin] = 1
                amount -= coin
                break
    return result

# встановлюємо велику суму
amount = 100000

# вимірюємо час виконання жадібного алгоритму
start_time = timeit.default_timer()
find_coins_greedy(amount)
end_time = timeit.default_timer()
greedy_time = end_time - start_time

# вимірюємо час виконання алгоритму динамічного програмування
start_time = timeit.default_timer()
find_min_coins(amount)
end_time = timeit.default_timer()
dp_time = end_time - start_time

print(f"Час виконання жадібного алгоритму: {greedy_time}")
print(f"Час виконання алгоритму динамічного програмування: {dp_time}")

# Висновок: алгоритм динамічного програмування працює значно повільніше, ніж жадібний алгоритм, оскільки він вимагає більше обчислень.