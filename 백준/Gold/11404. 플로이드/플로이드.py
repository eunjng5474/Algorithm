import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[int(1e9)] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i] = 0

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)   # 노선이 여러 개일 경우 최소 비용

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == int(1e9):
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()