import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = list(int(input()) for _ in range(N))
coins.reverse()
cnt = 0

for c in coins:
    if c <= K:
       cnt += K//c
       K %= c
    if not K:
        break
print(cnt)