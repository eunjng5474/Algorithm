import sys
import copy
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def dfs(x, y, cnt, arr):
    global result
    cnt += arr[x][y][0]
    arr[x][y][0] = 0
    result = max(cnt, result)

    # 1 ~ 16 물고기 위치 찾기
    for f in range(1, 17):
        fx, fy = -1, -1
        for k in range(4):
            for j in range(4):
                if arr[k][j][0] == f:
                    fx, fy = k, j
                    break

        # (-1, -1)이면 해당 번호의 물고기 없으므로 continue
        if fx == -1 and fy == -1:
            continue

        direc = arr[fx][fy][1]
        i = 0
        # for i in range(8):
        while i < 8:
            dir = (direc + i) % 8
            nx = fx + dx[dir]
            ny = fy + dy[dir]

            # (x, y)가 상어 위치이므로 (nx, ny) != (x, y)여야 한다. 
            if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == x and ny == y):
                arr[fx][fy][1] = dir
                arr[fx][fy], arr[nx][ny] = arr[nx][ny], arr[fx][fy]
                break
            i += 1
            # 이동 가능한 방향 찾을 때까지 회전하면서 최대 8번까지 확인
            # 회전하면 arr의 물고기 방향 바꿔줘야함!!


    # 물고기 모두 이동 후 상어 이동
    d = arr[x][y][1]
    for i in range(1, 5):   # 상어는 해당 방향에 대해 4번까지 이동 가능
        sx = x + dx[d] * i
        sy = y + dy[d] * i

        if 0 <= sx < 4 and 0 <= sy < 4 and 0 < arr[sx][sy][0]:
            dfs(sx, sy, cnt, copy.deepcopy(arr))



arr = [[] for _ in range(4)]
for a in range(4):
    lst = list(map(int, input().split()))
    for i in range(4):
        arr[a].append([lst[i*2], lst[i*2+1]-1])

result = 0
dfs(0, 0, 0, arr)
print(result)