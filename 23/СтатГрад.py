def f(x, y, mul):
    if x > y:
        return 0
    if x == y:
        # Должно обязательно содержать одно умножение!!!!!!!
        if mul:
            return 1
        else:
            return 0
    if mul:
        return f(x + 1, y, True) + f(x + 2, y, True)
    else:
        return f(x + 1, y, False) + f(x + 2, y, False) + f(x * 2, y, True) + f(x * 3, y, True)


print(f(1, 10, False))
