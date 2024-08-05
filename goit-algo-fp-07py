# імпортуємо потрібні бібліотеки
import random
import pandas as pd
from fractions import Fraction

# визначаємо кількість кидків
throws = 1000000

# створюємо словник для зберігання результатів
results = {i: 0 for i in range(2, 13)}

# виконуємо кидки
for _ in range(throws):
    dice1 = random.randint(1, 6)  # кидаємо перший кубик
    dice2 = random.randint(1, 6)  # кидаємо другий кубик
    total = dice1 + dice2  # обчислюємо суму чисел, які випали на кубиках
    results[total] += 1  # зберігаємо результат

# обчислюємо ймовірності
probabilities = {i: results[i] / throws for i in results}

# перетворюємо ймовірності у проценти та дроби, округлюємо дроби так, щоб чисельник був 1
probabilities_percent = {i: f"{probabilities[i]*100:.2f}% (1/{round(1/probabilities[i])})" for i in probabilities}

# створюємо dataframe для виведення результатів у вигляді таблиці
df = pd.DataFrame(list(probabilities_percent.items()), columns=['Сума', 'Ймовірність'])

# виводимо результати
print(df)

# вивід:
# 0      2  2.76% (1/36)
# 1      3  5.55% (1/18)
# 2      4  8.32% (1/12)
# 3      5  11.13% (1/9)
# 4      6  13.92% (1/7)
# 5      7  16.67% (1/6)
# 6      8  13.86% (1/7)
# 7      9  11.12% (1/9)
# 8     10  8.37% (1/12)
# 9     11  5.52% (1/18)
# 10    12  2.78% (1/36)

# Резульат схожий на аналітичну табличку, але відхилення є. Це пов'язано з кількістю кидків, яку ми виконали та рандомністю.