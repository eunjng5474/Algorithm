import sys
sys.setrecursionlimit(10**6)
from collections import deque

def BFS(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        start = q.popleft()
        for i in arr[start]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = start

N = int(input())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)


for i in range(N-1):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

BFS(1)
for v in visited[2:]:
    print(v)