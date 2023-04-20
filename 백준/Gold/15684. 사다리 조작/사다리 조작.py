import sys
input = sys.stdin.readline

def check():
    cnt = 0
    for i in range(1, N+1):
        chk = i
        for j in range(1, H+1):
            if arr[j][chk] == 1:
                chk += 1
            elif arr[j][chk-1] == 1:
                chk -= 1
        if chk == i:
            cnt += 1
    if cnt == N:   # 모든 세로선이 조건 충족해야 True!!!
        return True
    return False


def add_line(idx, add_cnt):  # 가로선 추가
    global result
    if add_cnt >= result:
        return

    if check():
        result = min(result, add_cnt)
        return

    for k in range(idx+1, len(possible)):
        x, y = possible[k]
        arr[x][y] = 1
        add_line(k, add_cnt+1)
        arr[x][y] = 0

    # for i in range(1, H+1):
    #     for j in range(1, N):
    #         if not arr[i][j]:
    #             if not arr[i][j-1] and not arr[i][j+1]:
    #                 arr[i][j] = 1
    #                 add_line(add_cnt+1)
    #                 arr[i][j] = 0


N, M, H = map(int, input().split())
arr =[[0] * (N+1) for _ in range(H+1)]
for m in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    # arr[a][b+1] = 1   # 이거 추가하면 연결 안 하는 두 세로선도 이어지게 됨
    # 그냥 1이면 오른쪽 이동
    # -1의 인덱스가 1이면 왼쪽으로 이동

possible = []
for i in range(1, H+1):
    for j in range(1, N):
        if not arr[i][j]:
            if not arr[i][j-1] and not arr[i][j+1]:
                possible.append((i, j))


result = 4
add_line(-1, 0)
if result > 3:
    result = -1

print(result)