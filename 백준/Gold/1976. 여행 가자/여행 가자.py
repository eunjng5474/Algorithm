import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        now = q.pop()
        for i in range(n):
            if arr[now][i] and not visited[i]:
                visited[i] = True
                q.append(i)

n = int(input())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))

visited = [False] * (n+1)
result = "YES"
bfs(plan[0] - 1)
for p in plan:
    if not visited[p-1]:
        result = "NO"
        break
print(result)