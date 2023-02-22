from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        if x == N-1 and y == M-1:
            break

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == '1' and visited[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt = 1

bfs(0, 0)
print(visited[N-1][M-1])
