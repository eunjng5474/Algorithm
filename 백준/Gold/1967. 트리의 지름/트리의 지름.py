import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(n, w):
    for next, weight in graph[n]:
        if visited[next] == -1:
            visited[next] = w + weight
            dfs(next, w + weight)


n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

visited = [-1] * (n+1)
visited[1] = 0
dfs(1, 0)
node = visited.index(max(visited))

visited = [-1] * (n+1)
visited[node] = 0
dfs(node, 0)
print(max(visited))