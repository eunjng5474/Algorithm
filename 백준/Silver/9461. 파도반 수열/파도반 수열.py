import sys

t = int(input())
dp = [[] for _ in range(101)]
dp[0] = 0
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, 101):
    dp[i] = dp[i-3] + dp[i-2]

for tc in range(t):
    n = int(input())
    print(dp[n])