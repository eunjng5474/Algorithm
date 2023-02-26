import sys
from collections import deque
sys.setrecursionlimit(10**6)

def DFS(start):
    global result1
    visited[start] = 1
    result1.append(start)
    for i in arr[start]:
        if visited[i] == 0:
            DFS(i)


def BFS(start):
    global result2
    q = deque()
    q.append(start)

    while q:
        start = q.popleft()
        visited[start] = 1
        result2.append(start)
        for i in arr[start]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1


N, M, V = map(int, input().split())
arr = [[] for _ in range(N+1)]

for m in range(M):
    u, v = map(int, sys.stdin.readline().split())
    arr[u].append(v)
    arr[v].append(u)

for i in arr:
    i.sort()

result1 = []
visited = [0] * (N+1)
DFS(V)
print(*result1)

result2 = []
visited = [0] * (N+1)
BFS(V)
print(*result2)
