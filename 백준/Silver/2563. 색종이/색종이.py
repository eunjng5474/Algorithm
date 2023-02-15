N = int(input())
arr = [[0] * 100 for _ in range(100)]

for n in range(N):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[a+i][b+j] = 1

cnt = 0
for a in arr:
    for i in range(100):
        if a[i] == 1:
            cnt += 1
print(cnt)