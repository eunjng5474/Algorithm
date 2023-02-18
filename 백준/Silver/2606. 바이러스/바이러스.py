def DFS_R(start):
    visited[start] = 1
    for i in arr[start]:
        if visited[i] == 0:
            DFS_R(i)

N = int(input())
P = int(input())
arr = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for p in range(P):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    
DFS_R(1)
result_r = visited.count(1) - 1
print(result_r)