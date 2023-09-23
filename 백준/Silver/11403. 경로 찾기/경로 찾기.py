import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(i):
    for j in range(n):
        if arr[i][j] and not visited[j]:
            visited[j] = 1
            dfs(j)

for i in range(n):
    visited = [0 for _ in range(n)]
    dfs(i)
    print(*visited)