import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visited = [False] * n
lst = []

def dfs():
    if len(lst) == m:
        print(*lst)
        return

    check = 0
    for i in range(n):
        if not visited[i] and check != nums[i]:
            visited[i] = True
            lst.append(nums[i])
            check = nums[i]
            dfs()
            visited[i] = False
            lst.pop()

dfs()