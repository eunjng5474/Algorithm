cnt = 0
def DFS(x, y):
    global cnt          
    arr[x][y] = 0
    cnt += 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == '1':
                DFS(nx, ny)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
arr = [list(input()) for _ in range(N)]
result_lst = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            cnt = 0
            DFS(i, j)
            result_lst.append(cnt)

result = sorted(result_lst)
print(len(result))
for i in result:
    print(i)