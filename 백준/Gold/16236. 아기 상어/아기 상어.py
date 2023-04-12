import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global shark
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    possible = []

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] <= shark and not visited[nx][ny]: # 이동 가능하면
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

                    if 0 < arr[nx][ny] < shark:     # 먹을 수 있으면
                        possible.append([visited[nx][ny]-1, nx, ny])  # 가능한 리스트에 추가

    possible.sort(key=lambda x:(x[0], x[1], x[2]))  # 거리-행-열 순으로 정렬
    return possible



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
shark = 2
cnt = 0
time = 0

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            x, y = i, j
            arr[i][j] = 0

while True:
    visited = [[0] * N for _ in range(N)]
    lst = bfs(x, y)

    if not lst:
        break

    dist, x, y = lst[0]
    cnt += 1
    time += dist

    if shark == cnt:
        shark += 1
        cnt = 0

    arr[x][y] = 0

print(time)