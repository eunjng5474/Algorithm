import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    cnt = 1
    q = deque()
    q.append(start)

    while q:
        start = q.popleft()
        visited[start] = cnt
        cnt += 1

        for i in arr[start]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = cnt

N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)
for m in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for a in arr:
    a.sort()

bfs(R)
for v in visited[1:]:
    print(v)