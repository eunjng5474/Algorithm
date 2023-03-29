from collections import deque
import sys
input = sys.stdin.readline

dx = [-2, -2, -1, -1, 2, 2, 1, 1]
dy = [-1, 1, -2, 2, -1, 1, -2, 2]

def bfs(sx, sy):
    # cnt = 1
    q = deque()
    q.append((sx, sy))
    arr[sx][sy] = 1
    while q:
        x, y = q.popleft()
        # arr[x][y] = cnt
        # cnt += 1

        if x == gx and y == gy:
            break

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < l and 0 <= ny < l and not arr[nx][ny]:
                # cnt += 1
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))



T = int(input())
for tc in range(T):
    l = int(input())
    arr = [[0] * l for _ in range(l)]
    sx, sy = (map(int, input().split()))
    gx, gy = map(int, input().split())
    # cnt = 0

    bfs(sx, sy)
    print(arr[gx][gy]-1)