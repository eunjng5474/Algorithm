import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
nums = []

def postorder(s, e):
    if s > e:
        return
    mid = e + 1

    for i in range(s+1, e+1):
        if nums[i] > nums[s]:
            mid = i
            break

    postorder(s+1, mid-1)       # 왼쪽
    postorder(mid, e)           # 오른쪽
    print(nums[s])


while True:
    try:
        nums.append(int(input()))
    except:
        break

postorder(0, len(nums)-1)