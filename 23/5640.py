"""
Исполнитель преобразует число на экране.
У исполнителя есть две команды, которые обозначены латинскими буквами:

A. Вычти 4
B. Вычти сумму цифр числа

Программа для исполнителя – это последовательность команд.
Сколько существует программ, для которых при исходном числе 36 результатом является число 2,
и при этом траектория вычислений содержит число 14?
Ответ: 7
"""


def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    return f(x - 4, y) + f(x - sum(int(i) for i in str(x)), y)


print(f(36, 14) * f(14, 2))
