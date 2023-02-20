from collections import deque

N, K = map(int, input().split())
queue = deque()
result = []
for i in range(1, N+1):
    queue.append(i)

cnt = 1
while queue:
    if cnt % K == 0:
        result.append(queue.popleft())
    else:
        x = queue.popleft()
        queue.append(x)
    cnt += 1
print('<', end='')
for r in range(len(result)-1):
    print(f'{result[r]}, ', end='')
print(result[-1], end='')
print('>')