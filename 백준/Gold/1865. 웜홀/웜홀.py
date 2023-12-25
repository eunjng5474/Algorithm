import sys
input = sys.stdin.readline

def bf(start):
    dist = [int(1e9)] * (n+1)
    dist[start] = 0

    for i in range(n):
        for s, e, t in graph:
            if t + dist[s] < dist[e]:
                dist[e] = t + dist[s]
                # 마지막에도 최단거리 갱신된다면 음의 사이클 존재
                if i == n - 1:
                    return True
    return False

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = []

    for i in range(m):
        s, e, t = map(int, input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))

    # 음의 가중치 -> 벨만 포드 
    for i in range(w):
        s, e, t = map(int, input().split())
        graph.append((s, e, -t))

    if bf(1):
        print("YES")
    else:
        print("NO")