H, W = map(int, input().split())
arr = [[0] * W for _ in range(H)]
block = list(map(int, input().split()))
for i in range(W):
    for j in range(block[i]):
        arr[H-1-j][i] = 1

result = 0
for i in range(H):
    for j in range(W):
        cnt = 0

        if arr[i][j]:
            while j < W-1:
                j += 1
                if arr[i][j] == 1:
                    result += cnt
                    break
                else:
                    cnt += 1

print(result)

