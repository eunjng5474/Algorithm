N = int(input())
nums = list(map(int, input().split()))
result = []

for i in range(N):
    result.insert(i-nums[i], i+1)
print(*result)