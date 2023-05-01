import sys
# sys.stdin = open('input_2239.txt')
input = sys.stdin.readline

def row_check(row, num):   # 가로 확인
    for col in range(9):
        if arr[row][col] == num:
            # 넣을 값(num)이 이미 그 줄에 있으면 False
            return False
    return True

def col_check(col, num):    # 세로 확인
    for row in range(9):
        if arr[row][col] == num:
            return False
    return True

def square_check(row, col, num):    # 사각형 확인
    r = row // 3 * 3    # 각 사각형의 첫번째 행/렬로 설정(0, 3, 6 중 1)
    c = col // 3 * 3

    for a in range(3):
        for b in range(3):
            if arr[r+a][c+b] == num:
                return False
    return True


def dfs(idx):
    if idx == len(zero_idx):
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end="")
            print()
        exit()

    x, y = zero_idx[idx]
    for n in range(1, 10):
        if row_check(x, n) and col_check(y, n) and square_check(x, y, n):
            arr[x][y] = n
            dfs(idx+1)
            arr[x][y] = 0


arr = [list(map(int, input().rstrip())) for _ in range(9)]
zero_idx = []
for i in range(9):
    for j in range(9):
        if not arr[i][j]:
            zero_idx.append((i, j))

dfs(0)