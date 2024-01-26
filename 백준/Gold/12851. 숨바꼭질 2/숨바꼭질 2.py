from collections import deque

def bfs(x):
    global cnt, result
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        now = q.popleft()
        if now == k:
            result = visited[now]
            cnt += 1
            continue

        for i in [now-1, now+1, now*2]:
            if i < 0 or i >= 100001:
                continue
            if not visited[i] or visited[i] == visited[now] + 1:
                visited[i] = visited[now] + 1
                q.append(i)


n, k = map(int, input().split())
visited = [0] * 100001
cnt, result = 0, 0
bfs(n)

print(result - 1)
print(cnt)