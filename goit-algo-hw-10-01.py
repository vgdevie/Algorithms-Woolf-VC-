from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

# ініціалізуємо модель
model = LpProblem(name="production-optimization", sense=LpMaximize)

# ініціалізуємо змінні
lemonade = LpVariable(name="lemonade", lowBound=0)
fruit_juice = LpVariable(name="fruit_juice", lowBound=0)

# додаємо обмеження
model += (2 * lemonade + fruit_juice <= 100, "water_constraint")
model += (lemonade <= 50, "sugar_constraint")
model += (lemonade <= 30, "lemon_juice_constraint")
model += (2 * fruit_juice <= 40, "fruit_puree_constraint")

# визначаємо цільову функцію
model += lemonade + fruit_juice

# вирішуємо задачу оптимізації
status = model.solve()

print(f"Статус: {LpStatus[model.status]}")
print(f"Оптимальна кількість виробленого лимонаду: {lemonade.varValue}")
print(f"Оптимальна кількість виробленого фруктового соку: {fruit_juice.varValue}")
print(f"Максимальна кількість вироблених продуктів: {model.objective.value()}")

# Оптимальна кількість виробленого лимонаду: 30.0
# Оптимальна кількість виробленого фруктового соку: 20.0
# Максимальна кількість вироблених продуктів: 50.0