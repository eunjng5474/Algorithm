import sys
input = sys.stdin.readline

def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:   # x의 부모보다 y의 부모가 상위 루트
        parent[x] = y   # x의 부모를 y의 부모로
    else:
        parent[y] = x

def find(x):
    if x == parent[x]:  # x가 부모노드이면 x 반환
        return x
    parent[x] = find(parent[x])     # 부모노드 탐색
    return parent[x]

n = int(input())
m = int(input())
parent = [i for i in range(n)]

for i in range(n):
    arr = list(map(int, input().split()))
    for j in range(n):
        if arr[j]:  # i, j 연결되어 있으면 union
            union(i, j)

plan = list(map(int, input().split()))
result = "YES"
for i in range(1, m):
    if parent[plan[i]-1] != parent[plan[0]-1]:
        # plan 중에서 부모노드가 계획의 첫번째 도시의 부모와 다른 경우 있으면 불가능
        result = "NO"
        break

print(result)