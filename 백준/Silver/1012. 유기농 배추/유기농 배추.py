import sys
sys.setrecursionlimit(10**6)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    arr[x][y] = 0

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < M and 0 <= ny < N:
            if arr[nx][ny] == 1:        
                # arr[nx][ny] = 0
                DFS(nx, ny)

    
T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * N for _ in range(M)]
    result = 0

    for k in range(K):
        a, b = map(int, input().split())
        arr[a][b] = 1


    cnt = 0
    for x in range(M):
        for y in range(N):
            if arr[x][y] == 1:
                cnt += 1
                DFS(x, y)

    print(cnt)   