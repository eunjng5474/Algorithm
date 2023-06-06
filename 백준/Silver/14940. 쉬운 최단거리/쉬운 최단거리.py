import sys

input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if arr[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
            # if not arr[nx][ny]:
            #     visited[nx][ny] = 0


# flag = False
for x in range(n):
    for y in range(m):
        if not arr[x][y]:
            visited[x][y] = 0
        if arr[x][y] == 2:
            bfs(x, y)
            # flag = True


for v in visited:
    print(*v)