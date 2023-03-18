import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 0 and visited[nx][ny] == 0:
            dfs(nx, ny)



N = int(input())
input_arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

max_height = 0
# min_height = 101
for i in range(N):
    if max(input_arr[i]) > max_height:
        max_height = max(input_arr[i])
    # if min(input_arr[i]) < min_height:
    #     min_height = min(input_arr[i])

for m in range(max_height):
    cnt = 0
    arr = []
    for n in range(N):
        arr.append(list(input_arr[n]))
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] <= m:
                arr[i][j] = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and visited[i][j] == 0:
                dfs(i, j)
                cnt += 1

    if cnt > result:
        result = cnt

print(result)
