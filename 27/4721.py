f = open('4721A.txt')
n, capacity, distance = map(int, f.readline().split())
points = []
for item in f:
    id_point, tube_count = map(int, item.split())
    box = tube_count // capacity + int(tube_count % capacity != 0)
    points.append((id_point, tube_count, box))
points.sort()

max_tubes = 0
max_box = 0
sum_tube = 0
sum_box = 0
start = end = 0

for i in range(n):
    while abs(points[start][0] - points[i][0]) > distance:
        sum_tube -= points[start][1]
        sum_box -= points[start][2]
        start += 1

    while end != n and abs(points[end][0] - points[i][0]) <= distance:
        sum_tube += points[end][1]
        sum_box += points[end][2]
        end += 1

    if sum_tube > max_tubes:
        max_tubes = sum_tube
        max_box = sum_box

print(max_box)

# Вариант I
"""for i in range(n):
    sum_tube = 0
    sum_box = 0
    for j in range(n):
        dist = abs(points[i][0] - points[j][0])
        if dist <= distance:
            sum_tube += points[j][1]
            sum_box += points[j][2]
    if sum_tube > max_tubes:
        max_tubes = sum_tube
        max_box = sum_box
print(max_box)"""
