import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    distance = [int(1e9)] * (n+1)
    hq = [(0, start)]
    distance[start] = 0

    while hq:
        dist, now = heapq.heappop(hq)
        if dist > distance[now]: continue

        for next, d in graph[now]:
            if dist + d < distance[next]:
                distance[next] = dist + d
                heapq.heappush(hq, (dist+d, next))

    return distance


n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

dist = dijkstra(1)
dist1 = dijkstra(v1)
dist2 = dijkstra(v2)

result1 = dist[v1] + dist1[v2] + dist2[n]   # 1 - v1 - v2 - n
result2 = dist[v2] + dist2[v1] + dist1[n]   # 1 - v2 - v1 - n

result = min(result1, result2)

if result >= int(1e9):
    print(-1)
else:
    print(result)