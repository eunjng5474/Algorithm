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

        for i in [x+1, x-1, x*2]:
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)
print(bfs(N))