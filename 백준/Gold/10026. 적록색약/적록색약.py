import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def no_check(x, y):
    q = deque()
    q.append((x, y))
    no_visited[x][y] = 1
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= N or ny < 0 or ny >= N or no_visited[nx][ny]:
                continue
            if arr[nx][ny] == arr[x][y]:
                no_visited[nx][ny] = 1
                q.append((nx, ny))

def yes_check(x, y, color):
    dq = deque()
    dq.append((x, y, color))
    yes_visited[x][y] = 1
    while dq:
        x, y, color = dq.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= N or ny < 0 or ny >= N or yes_visited[nx][ny]:
                continue
            if color == 'B' and arr[nx][ny] == 'B':
                yes_visited[nx][ny] = 1
                dq.append((nx, ny, color))

            elif color == 'R' or color == 'G':
                if arr[nx][ny] == 'R' or arr[nx][ny] == 'G':
                    yes_visited[nx][ny] = 1
                    dq.append((nx, ny, color))


N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
no_cnt = 0  # 적록색약 x
yes_cnt = 0 # o

no_visited = [[0] * N for _ in range(N)]
yes_visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not no_visited[i][j]:
            no_check(i, j)
            no_cnt += 1

        if not yes_visited[i][j]:
            yes_check(i, j, arr[i][j])
            yes_cnt += 1

print(no_cnt, yes_cnt)