from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    q = deque()
    q.append((a, ''))
    visited = [False for _ in range(10001)]

    while q:
        num, string = q.popleft()
        visited[num] = True

        if num == b:
            print(string)
            break

        d = (num * 2) % 10000
        if not visited[d]:
            visited[d] = True
            q.append((d, string+'D'))

        s = (num - 1) % 10000
        if not visited[s]:
            visited[s] = True
            q.append((s, string+'S'))

        l = (num % 1000) * 10 + num // 1000
        if not visited[l]:
            visited[l] = True
            q.append((l, string+'L'))

        r = (num % 10) * 1000 + num // 10
        if not visited[r]:
            visited[r] = True
            q.append((r, string+'R'))