"""
Исполнитель А16 преобразует число, записанное на экране.
У исполнителя есть три команды, которым присвоены номера:

1. Прибавить 1
2. Прибавить 2
3. Умножить на 2

Первая из них увеличивает число на экране на 1, вторая увеличивает его на 2, третья умножает его на 2.
Программа для исполнителя А16 – это последовательность команд.
Сколько существует таких программ, которые исходное число 3 преобразуют в число 12 и при этом траектория вычислений
программы содержит число 10?
"""


def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)


# Если программа должна идти через число 10
print(f(3, 10) * f(10, 12))