from collections import deque

N = int(input())
q = deque()
for i in range(1, N+1):
    q.append(i)

cnt = 1
while len(q) != 1:
    if cnt % 2:
        q.popleft()
    else:
        q.append(q.popleft())
    cnt += 1
print(*q)
