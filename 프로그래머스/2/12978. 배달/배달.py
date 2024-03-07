from heapq import heappush, heappop

def solution(N, road, K):
    answer = 0
    visited = [int(1e9)] * (N+1)
    graph = [[] for _ in range(N+1)]
    for r in road:
        graph[r[0]].append((r[2], r[1]))
        graph[r[1]].append((r[2], r[0]))

    def dijkstra(n):
        visited[n[1]] = 0
        q = []
        heappush(q, n)
        
        while q:
            time, now = heappop(q)
            if time > visited[now]:
                continue
            for i in graph[now]:
                tmp = time + i[0]
                if tmp < visited[i[1]]:
                    visited[i[1]] = tmp
                    heappush(q, (tmp, i[1]))
            
    dijkstra((0, 1))
    for i in range(1, N+1):
        if visited[i] <= K:
            answer += 1
    return answer