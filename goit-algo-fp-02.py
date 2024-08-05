import turtle

def draw_tree(t, branch_len, level):
    """
    Функція для малювання дерева Піфагора.

    t - об'єкт turtle
    branch_len - довжина гілки
    level - рівень рекурсії
    """
    if level == 0:
        t.forward(branch_len)
        t.backward(branch_len)
    else:
        t.forward(branch_len)

        t.left(45)
        draw_tree(t, branch_len / 2, level - 1)

        t.right(90)
        draw_tree(t, branch_len / 2, level - 1)

        t.left(45)
        t.backward(branch_len)

# створюємо об'єкт turtle
t = turtle.Turtle()

# отримуємо рівень рекурсії від користувача
level = int(input("введіть рівень рекурсії: "))

# встановлюємо початкову позицію
t.penup()
t.goto(-150, 90)
t.pendown()

# малюємо дерево
draw_tree(t, 100, level)

# затримуємо вікно відкритим
turtle.done()