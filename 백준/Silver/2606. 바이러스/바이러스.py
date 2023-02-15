N = int(input())
M = int(input())

visited = [0] * (N+1)
arr = [[0] * (N+1) for _ in range(N+1)]
stack = [1]

for m in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

while stack:
    start = stack.pop()

    if visited[start] == 0:
        visited[start] = 1
        
    for next in range(1, N+1):
        if arr[start][next] == 1 and visited[next] == 0:
            visited[next] = 1
            stack.append(next)
    
print(visited.count(1) - 1)