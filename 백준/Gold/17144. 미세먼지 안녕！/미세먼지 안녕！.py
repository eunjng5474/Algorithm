import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]      # 상하좌우
dy = [0, 0, -1, 1]

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

# 미세먼지 확산
def spread(x, y):
    n = arr[x][y] // 5
    cnt = 0 # 확산되는 칸 수 카운트

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or nx >= r or ny < 0 or ny >= c or arr[nx][ny] == -1:
            continue
        move[nx][ny] += n
        cnt += 1

    move[x][y] += arr[x][y] - (n * cnt)

def cleaner_up(x, y):   # 공청기 위쪽 순환
    direct = [0, 3, 1, 2]   # 상우하좌 - 위쪽 공기 순환 방향(우상좌하) 역순의 반대
    d = 0
    while True:
        if d == 4: break
        nx = x + dx[direct[d]]
        ny = y + dy[direct[d]]

        if nx < 0 or nx > air or ny < 0 or ny >= c:     # nx, ny가 순환 범위 벗어나면 방향 바꾸기
            d += 1
            continue

        if nx == air and ny == 0:   # 다음 좌표가 공청기면 해당 위치 0으로 바꾸고 종료
            move[x][y] = 0
            break
        move[x][y] = move[nx][ny]   # nx, ny 좌표값 가져오기
        x, y = nx, ny

def cleaner_down(x, y):     # 공청기 아래쪽 순환
    direct = [1, 3, 0, 2]   # 하우상좌
    d = 0
    while True:
        if d == 4: break
        nx = x + dx[direct[d]]
        ny = y + dy[direct[d]]

        if nx <= air or nx >= r or ny < 0 or ny >= c:     # nx, ny가 순환 범위 벗어나면 방향 바꾸기
            d += 1
            continue

        if nx == air+1 and ny == 0:   # 다음 좌표가 공청기면 해당 위치 0으로 바꾸고 종료
            move[x][y] = 0
            break
        move[x][y] = move[nx][ny]   # nx, ny 좌표값 가져오기
        x, y = nx, ny

        
# 공기청정기 윗 행 좌표
air = 0
for i in range(r):
    if arr[i][0] == -1:
        air = i
        break

for _ in range(t):
    arr[air][0] = arr[air+1][0] = -1
    move = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                spread(i, j)

    cleaner_up(air-1, 0)
    cleaner_down(air+2, 0)
    arr = move

result = 0
for i in arr:
    result += sum(i)
print(result)