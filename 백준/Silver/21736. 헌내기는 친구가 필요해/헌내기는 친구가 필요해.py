import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = list([0] * m for _ in range(n))
result = 0

def dfs():
    global result
    stack = []
    flag = False
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'I':
                stack.append((i, j))
                flag = True
                break
        if flag:
            break

    while stack:
        x, y = stack.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or arr[nx][ny] == 'X':
                continue

            if arr[nx][ny] == 'O' and not visited[nx][ny]:
                stack.append((nx, ny))
                visited[nx][ny] = 1
            if arr[nx][ny] == 'P' and not visited[nx][ny]:
                result += 1
                stack.append((nx, ny))
                visited[nx][ny] = 1

dfs()
if result:
    print(result)
else:
    print('TT')