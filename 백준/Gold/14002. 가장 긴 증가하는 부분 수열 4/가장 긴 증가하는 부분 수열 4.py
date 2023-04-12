import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
dp = [1] * N
result = []

for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            if dp[i] <= dp[j]+1:
                dp[i] = dp[j]+1

sol = max(dp)
for n in range(N):
    if dp[n] == sol:
        result.append(nums[n])
        cnt = sol-1
        j = n-1
        while j >= 0:
            if dp[j] == cnt:
                if result[-1] > nums[j]:
                    result.append(nums[j])
                    cnt -= 1
            j -= 1
        break

result.sort()
print(sol)
print(*result)