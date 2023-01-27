"""
Определите количество пятизначных чисел, записанных в девятеричной системе счисления,
которые не начинаются с нечетных цифр, не оканчиваются цифрами 1 или 8, а также содержат
в своей записи не более одной цифры 3.
"""
import itertools

list_string = itertools.product('012345678', repeat=5)
count = 0
for str in list_string:
    line = ''.join(str)
    if line.count('3') <= 1 and line[-1] not in '18' and line[0] not in '01357':
        count += 1
print(count)