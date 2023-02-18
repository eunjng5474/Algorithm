stack = []
def DFS_S(start):
    stack.append(start)    
    visited[start] = 1
    while stack:
        for i in arr[start]:
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1
        start = stack.pop()

N = int(input())
P = int(input())
arr = [[] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for p in range(P):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

DFS_S(1)
result_s = visited.count(1) - 1
print(result_s)