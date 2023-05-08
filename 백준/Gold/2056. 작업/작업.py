import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
in_degree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
times = [0] * (N+1)
dp = [0] * (N+1)

for n in range(N):
    t, num, *args = map(int, input().split())
    times[n+1] = t
    if num:
        for a in args:
            graph[a].append(n+1)
            in_degree[n+1] += 1

def topology():
    q = deque()
    for p in range(1, N+1):
        if not in_degree[p]:
            q.append(p)
            dp[p] = times[p]
    while q:
        now = q.popleft()
        for next in graph[now]:
            in_degree[next] -= 1
            if not in_degree[next]:
                q.append(next)
            dp[next] = max(dp[next], dp[now]+times[next])

topology()
print(max(dp))