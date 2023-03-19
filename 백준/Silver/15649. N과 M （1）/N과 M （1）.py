N, M = map(int, input().split())
nums = list(x for x in range(1, N+1))
lst = []
visited = [False] * (N+1)

def sol(n):
    if len(lst) == M:
        print(*lst)
        return
    else:
        for i in nums:
            if not visited[i]:
                visited[i] = True
                lst.append(i)
                sol(i+1)
                lst.pop()
                visited[i] = False

sol(1)