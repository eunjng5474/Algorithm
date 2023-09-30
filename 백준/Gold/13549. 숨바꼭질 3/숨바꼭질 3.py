import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
visited = [0 for _ in range(100001)]
visited[n] = 1
q = deque()
q.append(n)

while q:
    now = q.popleft()

    if now == k:
        break

    if now * 2 <= 100000 and not visited[now * 2]:
        visited[now * 2] = visited[now]
        q.appendleft(now * 2)
    if now - 1 >= 0 and not visited[now - 1]:
        visited[now - 1] = visited[now] + 1
        q.append(now - 1)
    if now + 1 <= 100000 and not visited[now + 1]:
        visited[now + 1] = visited[now] + 1
        q.append(now + 1)


print(visited[k] - 1)