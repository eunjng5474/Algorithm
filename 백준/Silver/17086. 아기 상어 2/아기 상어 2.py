import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1] # 상하좌우 좌상 우상 좌하 우하
dy = [0, 0, -1, 1, -1, 1, -1, 1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]
q = deque()
result = 0

def bfs():
    while q:
        x, y = q.popleft()
        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if not arr[nx][ny]:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))

            # if not arr[nx][ny]:
            #     visited[nx][ny] = visited[x][y] + 1
            #     q.append((nx, ny))


for x in range(N):
    for y in range(M):
        if arr[x][y]:
            q.append((x, y))
bfs()
for a in arr:
    result = max(max(a), result)
# for v in visited:
#     result = max(max(v), result)
print(result - 1)