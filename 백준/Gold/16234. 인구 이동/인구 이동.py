import sys
input = sys.stdin.readline
from collections import deque


dx = [0, 1, 0, -1] # 우하좌상
dy = [1, 0, -1, 0]

def bfs(x, y, num):
    global flag, xy_lst
    q = deque()
    q.append((x, y))
    visited[x][y] = num

    tmp_set = set()
    tmp_set.add((x, y))
    tmp_sum = arr[x][y]
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(arr[nx][ny] - arr[x][y]) <= R:
                    flag = True
                    visited[nx][ny] = num
                    q.append((nx, ny))
                    tmp_set.add((nx, ny))
                    tmp_sum += arr[nx][ny]

    xy_lst.append([tmp_sum, tmp_set])





N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
while True:
    visited = [[0] * N for _ in range(N)]

    xy_lst = []
    num = 0
    flag = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                num += 1
                bfs(i, j, num)

    if not flag:
        print(cnt)
        break

    cnt += 1
    for l in xy_lst:
        people = l[0] // len(l[1])
        for x, y in l[1]:
            arr[x][y] = people