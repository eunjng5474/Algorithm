N, M = map(int, input().split())
lst = []

def sol(n):
    if len(lst) == M:
        print(*lst)
        return
    else:
        for i in range(1, N+1):
            lst.append(i)
            sol(i+1)
            lst.pop()

sol(1)