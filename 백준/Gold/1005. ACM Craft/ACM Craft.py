import sys
input = sys.stdin.readline
from collections import deque

def topology():
    q = deque()
    for k in range(1, N+1):
        if not in_degree[k]:
            q.append(k)
            dp[k] = times[k]

    while q:
        now = q.popleft()
        for next in graph[now]:
            in_degree[next] -= 1
            if not in_degree[next]:
                q.append(next)
            dp[next] = max(dp[next], dp[now]+times[next])
                # dp[next] = min(dp[next], dp[now]+times[next])

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    dp = [0] * (N+1)
    # dp = [0] + [int(1e9)]*N
    in_degree = [0] * (N+1)

    for k in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        in_degree[y] += 1

    topology()
    W = int(input())
    print(dp[W])