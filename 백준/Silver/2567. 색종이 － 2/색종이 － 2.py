dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

stack = []
def dfs(x, y):
    global cnt
    stack.append((x, y))
    visited[x][y] = 1

    while stack:
        x, y = stack.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < 101 and 0 <= ny < 101 and visited[nx][ny] == 0:
                if arr[nx][ny] == 1:
                    stack.append((nx, ny))
                    visited[nx][ny] = 1
                else:
                    cnt += 1


N = int(input())
arr = [[0] * 101 for _ in range(101)]
visited = [[0] * 101 for _ in range(101)]
cnt = 0

for n in range(N):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[a+i][b+j] = 1

for x in range(101):
    for y in range(101):
        if arr[x][y] == 1 and visited[x][y] == 0:
            dfs(x, y)
print(cnt)