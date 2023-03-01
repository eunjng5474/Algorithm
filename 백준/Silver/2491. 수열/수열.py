import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

result = []
plus = 1
minus = 1

for i in range(N-1):
    if nums[i+1] >= nums[i]:
        plus += 1
    else:
        result.append(plus)
        plus = 1
result.append(plus)

for j in range(N-1):
    if nums[j+1] <= nums[j]:
        minus += 1
    else:
        result.append(minus)
        minus = 1
result.append(minus)

print(max(result))