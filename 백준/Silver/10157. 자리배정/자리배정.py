import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0] # 상우하좌
dy = [0, 1, 0, -1]

C, R = map(int, input().split())
K = int(input())
arr = [[0] * C for _ in range(R)]
d = 0
x, y = R-1, 0
cnt = 1
arr[x][y] = cnt

if K > C * R:
     print(0)
else:
    while cnt != K:
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] == 0:
            cnt += 1
            arr[nx][ny] = cnt
            x, y = nx, ny
        else:
            d += 1
            if d == 4:
                d = 0
    print(y+1, R-x)