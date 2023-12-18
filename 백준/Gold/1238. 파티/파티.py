import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    times[start] = 0

    while q:
        t, now = heapq.heappop(q)   # 소요시간, 현재 위치
        for next, time in graph[now]:   # now에서 갈 수 있는 곳 중
            cost = t + time             # now까지의 값 + now에서 next까지의 시간이
            if cost < times[next]:       # 기존 저장된 값보다 작으면 갱신 후 push
                times[next] = cost
                heapq.heappush(q, (cost, next))


n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))

result = 0
for i in range(1, n+1):
    if i == x: continue
    tmp = 0

    times = [int(1e9)] * (n + 1)
    dijkstra(i)
    tmp += times[x]     # i에서 x까지 소요 시간

    times = [int(1e9)] * (n + 1)
    dijkstra(x)
    tmp += times[i]     # x에서 i까지 소요 시간

    result = max(result, tmp)
print(result)