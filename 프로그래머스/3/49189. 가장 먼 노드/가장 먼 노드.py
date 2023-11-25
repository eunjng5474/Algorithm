from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    q = deque()
    q.append(1)
    visited[1] = 1
    
    while q:
        now = q.popleft()
        for next in graph[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = visited[now] + 1
    
    answer = visited.count(max(visited))
    return answer