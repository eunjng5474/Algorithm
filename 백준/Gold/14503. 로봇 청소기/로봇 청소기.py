import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]  # 북동남서
dy = [0, 1, 0, -1]

def sol(x, y, d):
    global cnt
    if not arr[x][y]:
        arr[x][y] = 2
        cnt += 1

    for i in range(4):
        nd = (d + 3) % 4    # 반시계 회전
        nx = x + dx[nd]
        ny = y + dy[nd]

        if not arr[nx][ny]:
            sol(nx, ny, nd)
            return
        # 방향 변경
        d = nd

    nd = (d + 2) % 4    # 후진
    nx = x + dx[nd]
    ny = y + dy[nd]

    if arr[nx][ny] == 1:  # 후진 불가
        return

    sol(nx, ny, d)


n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


cnt = 0
sol(r, c, d)
print(cnt)