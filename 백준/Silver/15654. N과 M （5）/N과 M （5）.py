N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * N
result = []
lst = []

def sol(n):
    if len(lst) == M:
        print(*lst)
        # result.append(lst)
        # result.append()
        return
    else:
        for i in range(N):
            if not visited[i]:
                lst.append(nums[i])
                visited[i] = True
                sol(i+1)
                lst.pop()
                visited[i] = False

sol(0)