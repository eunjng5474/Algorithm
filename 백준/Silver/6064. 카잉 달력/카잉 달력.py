import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())

    k = x
    while k <= m * n:
        if not ((k - x) % m) and not ((k - y) % n):
            break
        k += m

    if k > m * n:
        print(-1)
    else:
        print(k)