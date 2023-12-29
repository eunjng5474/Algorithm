import sys
input = sys.stdin.readline

def sol(num):
    if len(lst) == m:
        print(*lst)
        return

    for i in range(num, n):
        lst.append(nums[i])
        sol(i)
        lst.pop()

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
lst = []
sol(0)