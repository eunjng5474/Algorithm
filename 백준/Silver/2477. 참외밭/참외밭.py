import sys
input = sys.stdin.readline

K = int(input())
lst = [list(map(int, input().split())) for _ in range(6)]

big_w = 0
big_h = 0
small_w = 0
small_h = 0

for i in range(6):
    d, n = lst[i]
    if i % 2:
        if n > big_w:
            big_w = n
    else:
        if n > big_h:
            big_h = n

for i in range(6):
    if i % 2:
        if lst[(i-1) % 6][1] + lst[(i+1) % 6][1] == big_h:
            small_w = lst[i][1]
    else:
        if lst[(i-1) % 6][1] + lst[(i+1) % 6][1] == big_w:
            small_h = lst[i][1]

result = (big_h * big_w) - (small_h * small_w)
print(result * K)