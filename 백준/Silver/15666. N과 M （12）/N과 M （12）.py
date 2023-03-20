N, M = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))
result = []
lst = [0]

def sol(n):
    if len(lst) == M+1:
        print(*lst[1:])
        return
    else:
        for i in range(len(nums)):
            if lst[-1] <= nums[i]:
                lst.append(nums[i])
                sol(i + 1)
                lst.pop()

sol(1)