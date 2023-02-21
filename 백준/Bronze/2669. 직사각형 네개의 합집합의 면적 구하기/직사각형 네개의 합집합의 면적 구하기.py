arr = [[0] * 100 for _ in range(100)]
for d in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x2-x1):
        for j in range(y2-y1):
            arr[x1+i][y1+j] = 1

cnt = 0
for a in arr:
    for b in a:
        if b == 1:
            cnt +=1

print(cnt)