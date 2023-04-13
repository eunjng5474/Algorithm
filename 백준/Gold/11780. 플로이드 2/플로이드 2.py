import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[int(1e9)] * (N+1) for i in range(N+1)]
path = [[[i] for j in range(N+1)] for i in range(N+1)]

for a in range(1, N+1):
    graph[a][a] = 0
    path[a][a] = []


for m in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])


for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

                path[i][j] = path[i][k] + path[k][j]

for a in range(1, N+1):
    for b in range(1, N+1):
        if graph[a][b] == int(1e9):
            graph[a][b] = 0


for g in graph[1:]:
    print(*g[1:])



for i in range(1, N+1):
    for j in range(1, N+1):
        if not graph[i][j]:
            print(0)
        else:
            print(len(path[i][j])+1, end=" ")
            print(*path[i][j], end=" ")
            print(j)