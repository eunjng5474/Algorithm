import sys
input = sys.stdin.readline
from collections import deque

def topology():
    q = deque()
    for p in range(1, N+1):
        if not in_degree[p]:
            q.append(p)
            result[p] = 1

    while q:
        now = q.popleft()
        for next in graph[now]:    # now에서 갈 수 있는 곳 
            in_degree[next] -= 1   # 진입 차수 -= 1 
            if not in_degree[next]: # 진입차수 == 0이면 (갈 수 있으면)
                q.append(next)
                result[next] = result[now] + 1
                # q에 추가하고 now의 다음 학기에 들을 수 있음 



N, M = map(int, input().split())
in_degree = [0] * (N+1)   # 진입차수
graph = [[] for _ in range(N+1)]
result = [0] * (N+1)      # 이수 가능 학기 

for m in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

topology()
print(*result[1:])