import sys, copy
input = sys.stdin.readline

n = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

max_tmp = [0] * 3
min_tmp = [0] * 3

for i in range(n):
    a, b, c = map(int, input().split())

    for j in range(3):
        max_tmp[0] = a + max(max_dp[0], max_dp[1])
        min_tmp[0] = a + min(min_dp[0], min_dp[1])

        max_tmp[1] = b + max(max_dp[0], max_dp[1], max_dp[2])
        min_tmp[1] = b + min(min_dp[0], min_dp[1], min_dp[2])

        max_tmp[2] = c + max(max_dp[1], max_dp[2])
        min_tmp[2] = c + min(min_dp[1], min_dp[2])

    max_dp = copy.deepcopy(max_tmp)
    min_dp = copy.deepcopy(min_tmp)

print(max(max_dp), min(min_dp))