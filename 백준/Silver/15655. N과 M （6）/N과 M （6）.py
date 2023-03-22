N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

lst = []
def sol(n):
    if len(lst) == M:
        print(*lst)
        return
    else:
        for i in range(n, N):
            lst.append(nums[i])
            sol(i+1)
            lst.pop()

sol(0)