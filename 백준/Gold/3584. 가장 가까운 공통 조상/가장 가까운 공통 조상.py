import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    parent = [0] * (N+1)

    for n in range(N-1):
        a, b = map(int, input().split())
        parent[b] = a

    n1, n2 = map(int, input().split())

    lst = []
    i, j = n1, n2
    while True:
        if i == 0:
            break
        lst.append(i)
        i = parent[i]

    while j:
        if j in lst:
            result = j
            break
        j = parent[j]

    print(result)