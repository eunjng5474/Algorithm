import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
result = int(1e9)
visited = [0] * 100001

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        x = q.popleft()
        if x == K:
            return visited[x] - 1
        if x+1 <= 100000 and not visited[x+1]:
            visited[x+1] = visited[x] + 1
            q.append(x+1)
        if x - 1 >= 0 and not visited[x-1]:
            visited[x-1] = visited[x] + 1
            q.append(x-1)
        if x*2 <= 100000 and not visited[x*2]:
            visited[x*2] = visited[x] + 1
            q.append(x*2)

print(bfs(N))