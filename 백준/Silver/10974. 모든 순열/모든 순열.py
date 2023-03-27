N = int(input())

lst = []
visited = [0] * (N+1)
def sol(n):
    if len(lst) == N:
        print(*lst)
        return
    else:
        for i in range(1, N+1):
            if not visited[i]:
                lst.append(i)
                visited[i] = 1
                sol(i+1)
                lst.pop()
                visited[i] = 0

sol(1)