n = int(input())
max_x = max_y = -10000
min_x = min_y = 10000

for _ in range(n):
    x, y = map(int, input().split())
    if x > max_x: max_x = x
    if x < min_x: min_x = x
    if y > max_y: max_y = y
    if y < min_y: min_y = y

print((max_x - min_x) * (max_y - min_y))