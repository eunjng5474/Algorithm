from collections import deque
import sys
input = sys.stdin.readline

def bfs(idx):
    q = deque()
    q.append(idx)
    visited[idx] = 1

    while q:
        now = q.popleft()
        for next in friends[now]:
            if not visited[next]:
                visited[next] = visited[now] + 1
                q.append(next)


n, m = map(int, input().split())
friends = [[] for _ in range(n+1)]
result = n+1
cnt = 1e9

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

for i in range(1, n+1):
    visited = [0] * (n + 1)
    bfs(i)
    if sum(visited) < cnt:
        result = i
        cnt = sum(visited)

print(result)