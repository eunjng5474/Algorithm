import sys
sys.setrecursionlimit(10**5)


def DFS(start):
    global cnt
    visited[start] = 1
    for i in arr[start]:
        if visited[i] == 0:
            DFS(i)


N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0

for m in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

cnt = 0
for j in range(1, N+1):
    if visited[j] == 0:
        DFS(j)
        cnt += 1

print(cnt)