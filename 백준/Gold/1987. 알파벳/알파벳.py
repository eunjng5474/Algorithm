import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, cnt):
    global result
    result = max(result, cnt)

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or nx >= r or ny < 0 or ny >= c or check[ord(board[nx][ny]) - 65]:
            continue
        check[ord(board[nx][ny]) - 65] = True
        dfs(nx, ny, cnt+1)
        check[ord(board[nx][ny]) - 65] = False


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
check = [False] * 26
result = 0

check[ord(board[0][0]) - 65] = True
dfs(0, 0, 1)
print(result)