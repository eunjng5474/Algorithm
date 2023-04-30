import sys
input = sys.stdin.readline

C = int(input())
for c in range(C):
    nums = list(map(int, input().split()))
    n = nums.pop(0)
    avg = sum(nums) / n 
    cnt = 0
    for i in nums:
        if i > avg:
            cnt += 1
    result = cnt / n * 100
    print(f'{result:.3f}%')