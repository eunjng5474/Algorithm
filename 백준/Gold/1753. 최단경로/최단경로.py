import sys
input = sys.stdin.readline
from heapq import heappop, heappush

def sol(n):
    visited[n[1]] = 0
    q = []
    heappush(q, n)
    while q:
        cost, now = heappop(q)
        if cost > visited[now]:
            continue
        for i in node[now]:
            result = cost + i[0]
            if result < visited[i[1]]:
                visited[i[1]] = result
                heappush(q, (result, i[1]))



V, E = map(int, input().split())
K = int(input())
node = [[] for _ in range(V+1)]
visited = [int(1e9)] * (V+1)

for e in range(E):
    u, v, w = map(int, input().split())
    node[u].append((w, v))      # u노드에 (가중치 w, 도착 정점v) 저장

# print(node)
sol((0, K))
for v in visited[1:]:
    if v == int(1e9):
        print('INF')
    else:
        print(v)