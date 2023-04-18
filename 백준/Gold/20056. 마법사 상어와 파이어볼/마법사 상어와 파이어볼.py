import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
# arr = [[[0, 0, 0, 0, 0] for i in range(N)] for _ in range(N)]
arr = [[[] for _ in range(N)] for _ in range(N)]

# 질량, 속력, 방향, 이동 여부
for m in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append([m, s, d])

while K:
    K -= 1
    # 이동할 때 마다 새로운 배열 생성해서 집어넣기
    # 기존 배열에 저장하면 이동 전의 값과 이동 후에 값이 겹치면 중복으로 인식할 수 있음
    # 따라서 매번 이동한 위치 저장할 board 생성
    board = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if not arr[x][y]:
                continue

            for k in arr[x][y]:
                if not k[0]:
                    continue
                # 굳이 범위 초과할 때도 조건 안 주고 처음부터 % 사용해도 됨
                nx = (x + dx[k[2]] * k[1]) % N
                ny = (y + dy[k[2]] * k[1]) % N

                board[nx][ny].append([k[0], k[1], k[2]])

    for i in range(N):
        for j in range(N):
            if len(board[i][j]) >= 2:   # 합쳐질 때
                mm, ss = 0, 0
                dd = 1
                ll = len(board[i][j])
                odd_cnt = 0
                even_cnt = 0
                for p in board[i][j]:
                    mm += p[0]
                    ss += p[1]
                    if p[2] % 2:
                        odd_cnt += 1
                    else:
                        even_cnt += 1

                if odd_cnt == ll or even_cnt == ll:
                    dd = 0

                board[i][j] = []
                for d in range(4):
                    board[i][j].append([mm//5, ss//ll, dd+2*d])

    # board에만 바뀐 값 저장되어 있으므로 arr에 저장하기
    for i in range(N):
        for j in range(N):
            arr[i][j] = board[i][j]


result = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            for k in arr[i][j]:
                result += k[0]

print(result)