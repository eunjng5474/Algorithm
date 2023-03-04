import sys
input = sys.stdin.readline

N = int(input())
arr = [[0] * 101 for _ in range(101)]
for n in range(N):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[a+i][b+j] = 1

result = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] != arr[i][j+1]:
            result += 1

arr_rev = list(map(list, zip(*arr)))
for i in range(100):
    for j in range(100):
        if arr_rev[i][j] != arr_rev[i][j+1]:
            result += 1

print(result)