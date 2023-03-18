N, M = map(int, input().split())
lst = []

def sol(n):
    # lst.append(n)
    if len(lst) == M:
        print(*lst)
        return
    else:
        for i in range(n+1, N+1):
            lst.append(i)
            sol(i)
            lst.pop()
            
sol(0)