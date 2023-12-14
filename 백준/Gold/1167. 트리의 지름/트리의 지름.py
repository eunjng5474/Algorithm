from collections import deque
import sys
input = sys.stdin.readline

v = int(input())
tree = [[] for _ in range(v+1)]

for _ in range(v):
    nums = list(map(int, input().split()))
    for i in range(1, len(nums)-2, 2):
        tree[nums[0]].append([nums[i], nums[i+1]])

def bfs(x):
    visited = [-1] * (v+1)
    q = deque()
    q.append(x)
    visited[x] = 0
    dist = [0, 0]   # 거리 가장 큰 노드 번호, 거리

    while q:
        now = q.popleft()
        for a, b in tree[now]:
            if visited[a] == -1:
                visited[a] = visited[now] + b
                q.append(a)

                if visited[a] > dist[1]:
                    dist = [a, visited[a]]

    return dist

node = bfs(1)[0]   # 1번 노드 기준으로 가장 먼 노드의 번호
print(bfs(node)[1])     # 그 노드에서 가장 먼 노드의 거리 출력