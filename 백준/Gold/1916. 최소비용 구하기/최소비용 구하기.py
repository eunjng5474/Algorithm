import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
M = int(input())

line = [[] for _ in range(N+1)]  # 노드 인덱스에 대한 도착노드, 비용 저장할 리스트
visited = [int(1e9)] * (N+1)     # 노드별 최소비용 저장

for m in range(M):
    s, e, c = map(int, input().split())
    line[s].append((e, c))
start, end = map(int, input().split())


def sol(n):
    q = []
    heappush(q, n)      # q에 (노드, 비용) 추가
    while q:
        now, cost = heappop(q)      # 현재 노드, 비용
        if cost > visited[now]:     # pop한 cost가 visited[now]에 저장된 값보다 비싸면 pass
            continue
        for i in line[now]:         # 현재 노드에서 갈 수 있는 노드들에 대해서
            result = cost + i[1]    # cost + line에 저장된 i의 cost
            if result < visited[i[0]]:  # 그 값이 visited의 다음 노드에 저장된 값보다 작을 경우
                visited[i[0]] = result  # visited에 result 저장
                heappush(q, (i[0], result))     # q에 다음 노드와 result push

sol((start, 0))     # 시작 노드, 시작 비용(0)
print(visited[end])