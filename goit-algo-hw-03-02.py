import turtle

def koch_snowflake(t, order, size):
    """
    Функція для малювання сніжинки Коха.

    t - об'єкт turtle
    order - рівень рекурсії
    size - довжина сторони
    """
    if order == 0:
        # просто рухаємося вперед, якщо рівень рекурсії 0
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            # рекурсивно малюємо кожну сторону сніжинки
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

# створюємо об'єкт turtle
t = turtle.Turtle()

# отримуємо рівень рекурсії від користувача
order = int(input("введіть рівень рекурсії: "))

# встановлюємо початкову позицію
t.penup()
t.goto(-150, 90)
t.pendown()

for _ in range(3):
    # малюємо сніжинку
    koch_snowflake(t, order, 300)
    t.right(120)

# затримуємо вікно відкритим
turtle.done()