import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global result
    q = deque()
    tmp = 0
    cnt_0 = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                q.append((i, j))
            elif arr[i][j] == 0:
                cnt_0 += 1
    if cnt_0 == 0:
        result = 0
        return

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    cnt = arr[x][y] + 1
                    arr[nx][ny] = cnt
                    if cnt > tmp:
                        tmp = cnt
                    q.append((nx, ny))

    result = tmp - 1



def check():
    global result
    tmp = 0
    for i in range(N):
        tmp += arr[i].count(0)
    if tmp:
        result = -1





M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 1000 * 1000
cnt = 0


bfs()
check()
print(result)