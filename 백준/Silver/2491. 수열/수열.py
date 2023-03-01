import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

result = 0
plus = 1
minus = 1
for i in range(N-1):
    if nums[i+1] >= nums[i]:
        plus += 1
    else:
        if plus > result:
            result = plus
        plus = 1
if plus > result:
    result = plus

for j in range(N-1):
    if nums[j+1] <= nums[j]:
        minus += 1
    else:
        if minus > result:
            result = minus
        minus = 1
if minus > result:
    result = minus

print(result)