import sys
input = sys.stdin.readline

dp = [1] * 100001

for i in range(2, 100001):
    dp[i] += dp[i-2]

for i in range(3, 100001):
    dp[i] += dp[i-3]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])