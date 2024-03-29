import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

tetris=[[(0,0), (1,0), (0,1), (1,1)], # 정사각형
    [(0,0), (0,1), (0,2), (0,3)],  # 가로 직사각형
    [(0,0), (1,0), (2,0), (3,0)],  # 세로 직사각형
    [(0,0), (1,0), (2,0), (2,1)],  # 세로 긴 ㄴ
    [(0,1), (1,1), (2,1), (2,0)],  # 반대
    [(0,0), (0,1), (1,1), (2,1)],  # 세로 긴 ㄱ
    [(0,0), (0,1), (1,0), (2,0)],  # 반대
    [(0,0), (1,0), (1,1), (1,2)],  # 가로 긴 ㄴ
    [(1,0), (1,1), (1,2), (0,2)],  # 반대
    [(0,0), (0,1), (0,2), (1,2)],  # 가로 긴 ㄱ
    [(0,0), (0,1), (0,2), (1,0)],  # 반대
    [(0,1), (1,0), (1,1), (1,2)],  # ㅗ
    [(0,0), (0,1), (0,2), (1,1)],  # ㅜ
    [(0,0), (1,0), (1,1), (2,0)],  # ㅏ
    [(0,1), (1,1), (1,0), (2,1)],  # ㅓ
    [(0,0), (1,0), (1,1), (2,1)],
    [(0,1), (1,1), (1,0), (2,0)],
    [(1,0), (1,1), (0,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]]


def sol(x, y):
    global result
    for t in tetris:
        tmp = 0
        for d in t:
            nx = x + d[0]
            ny = y + d[1]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            tmp += arr[nx][ny]
        result = max(result, tmp)

for x in range(N):
    for y in range(M):
        sol(x, y)

print(result)