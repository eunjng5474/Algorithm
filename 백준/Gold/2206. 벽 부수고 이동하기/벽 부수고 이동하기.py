from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    visited[x][y][0] = 1
    while q:
        x, y, wall = q.popleft()

        if x == N-1 and y == M-1:
            return visited[x][y][wall]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][wall]:
                if not arr[nx][ny]:
                    visited[nx][ny][wall] = visited[x][y][wall]+1
                    q.append((nx, ny, wall))
                if not wall and arr[nx][ny]:
                    visited[nx][ny][1] = visited[x][y][wall]+1
                    q.append((nx, ny, 1))
    return -1



N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

print(bfs(0, 0))