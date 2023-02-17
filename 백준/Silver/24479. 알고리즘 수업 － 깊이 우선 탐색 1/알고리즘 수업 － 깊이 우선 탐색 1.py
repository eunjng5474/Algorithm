import sys
sys.setrecursionlimit(10**5)

def DFS(start):
    global cnt
    visited[start] = cnt
    for i in arr[start]:
        if visited[i] == 0:
            cnt += 1
            DFS(i) 

N, M, R = map(int, input().split())
visited = [0] * (N+1)
arr = [[] for _ in range(N+1)]
cnt = 1

for m in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(N+1):
    arr[i].sort()

DFS(R)
for j in range(1, N+1):
    print(visited[j])