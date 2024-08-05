import numpy as np

# функція та межі інтегрування
def f(x):
    return x ** 2

a = 0  # нижня 
b = 2  # верхня 

# Кількість випадкових точок
N = 1000000

x = np.random.uniform(a, b, N)
y = np.random.uniform(0, b**2, N)

# чи знаходяться точки під графіком
under_curve = y < f(x)

# відношення точок під графіком до загальної кількості точок
ratio = np.sum(under_curve) / N

integral = ratio * (b**2 - 0) * (b - a)

print("Інтеграл (Метод Монте-Карло): ", integral) 
# 2.669504