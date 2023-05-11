import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
# 위, 아래도 고려해야 함
dz = [0, 0, 0, 0, -1, 1]

def bfs(arr):
    q = deque()
    zero_cnt = 0
    for h in range(H):
        for x in range(N):
            for y in range(M):
                if arr[h][x][y] == 1:
                    q.append((h, x, y))
                    # visited[h][x][y] = 1
                if arr[h][x][y] == 0:
                    zero_cnt += 1
    if not zero_cnt:
        return 0

    while q:
        h, x, y = q.popleft()

        for d in range(6):
            nh = h + dz[d]
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or nh < 0 or nh >= H:
                continue
            if not arr[nh][nx][ny]:
                arr[nh][nx][ny] = arr[h][x][y] + 1
                q.append((nh, nx, ny))

    return check(arr)



def check(arr):
    max_n = 0
    for h in range(H):
        for i in range(N):
            if 0 in arr[h][i]:
                return -1
            max_n = max(max_n, max(arr[h][i]))
    return max_n


M, N, H = map(int, input().split())
arr = []
for h in range(H):
    tmp_arr = [list(map(int, input().split())) for _ in range(N)]
    arr.append(tmp_arr)
# visited = [[[0]*M for _ in range(N)] for _ in range(H)]
result = bfs(arr)
if result > 0:
    result -= 1
print(result)