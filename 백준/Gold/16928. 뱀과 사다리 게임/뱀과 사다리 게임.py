from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
move = {}
for _ in range(n+m):
    a, b = map(int, input().split())
    move[a] = b

result = 100
visited = [0] * 101

def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1
    while q:
        now = q.popleft()
        if now == 100:
            print(visited[now] - 1)
            break
        for n in range(1, 7):
            next = now + n
            if next in move:
                next = move[next]
            if next > 100 or visited[next]:
                continue

            visited[next] = visited[now] + 1
            q.append(next)

bfs()
