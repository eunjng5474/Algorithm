import sys
sys.setrecursionlimit(10**6)

def DFS_R(start):
    global cnt
    cnt += 1
    visited[start] = cnt
    for i in arr[start]:
        if visited[i] == 0:
            visited[i] = cnt
            DFS_R(i)

N, M, R = map(int, input().split())
arr = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1) 
cnt = 0

for m in range(M):
    u, v = map(int, sys.stdin.readline().rstrip().split())
    arr[u].append(v)
    arr[v].append(u)

for i in range(len(arr)):
    arr[i].sort()

DFS_R(R)
for i in visited[1:]:
    print(i)