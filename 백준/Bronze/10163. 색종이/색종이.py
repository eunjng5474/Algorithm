import sys

arr = [[0] * 1001 for _ in range(1001)]
N = int(input())
cnt = 1
for n in range(N):
    r, c, w, h = map(int, sys.stdin.readline().split())

    for i in range(w):
        for j in range(h):
            arr[r+i][c+j] = cnt
    cnt += 1

for i in range(1, N+1):
    result = 0
    for a in arr:
        result += a.count(i)
    print(result)