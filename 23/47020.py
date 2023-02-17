def f(x, y, pre):
    if x > y:
        return 0
    if x == y:
        return 1
    if pre:
        return f(x + 1, y, False) + f(x + 2, y, False)
    else:
        return f(x + 1, y, False) + f(x + 2, y, False) + f(x * 2, y, True)


print(f(1, 9, False))
