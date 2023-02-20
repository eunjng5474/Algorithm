import sys
sys.setrecursionlimit(10**6)

def DFS(start):
    global cnt
    cnt += 1
    visited[start] = cnt
    for i in arr[start]:
        if visited[i] == 0:
            DFS(i)


N, M, R = map(int, input().split())
arr = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for m in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    arr[u].append(v)
    arr[v].append(u)

for a in arr:
    a.sort(reverse=True)
cnt = 0
DFS(R)

for v in visited[1:]:
    print(v)