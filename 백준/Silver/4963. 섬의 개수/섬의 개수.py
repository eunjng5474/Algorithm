import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < h and 0 <= ny < w:
                if arr[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    result = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] and not visited[i][j]:
                result += 1
                bfs(i, j)
    print(result)