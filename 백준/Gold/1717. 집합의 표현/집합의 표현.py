import sys
input = sys.stdin.readline

def find_set(x):
    if rep[x] == x:
        return x
    rep[x] = find_set(rep[x])
    return rep[x]

def union(x, y):
    rep[find_set(y)] = find_set(x)


n, m = map(int, input().split())
rep = [i for i in range(n+1)]
for tc in range(m):
    num, a, b = map(int, input().split())
    if num == 0:
        union(a, b)
    else:
        if find_set(a) == find_set(b):
            print("YES")
        else:
            print("NO")