from collections import deque

# функція для перевірки, чи є рядок паліндромом
def is_palindrome(s):
    s = ''.join(s.lower().split())
    d = deque(s)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

# тестуємо
test_string = "кит на морі романтик"
if is_palindrome(test_string):
    print(f"Рядок '{test_string}' є паліндромом")
else:
    print(f"Рядок '{test_string}' не є паліндромом")