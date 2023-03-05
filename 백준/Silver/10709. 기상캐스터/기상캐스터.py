H, W = map(int, input().split())
arr = [list(input()) for _ in range(H)]
result = [[-1] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if arr[i][j] == 'c':
            result[i][j] = 0
        else:
            cnt = 0
            x, y = i, j
            while y > 0:
                y -= 1
                cnt += 1
                if arr[x][y] == 'c':
                    result[i][j] = cnt
                    break

for r in result:
    print(*r)