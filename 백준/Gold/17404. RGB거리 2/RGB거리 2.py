import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = int(1e9)

for k in range(3):
    dp = [[[0] for i in range(3)] for _ in range(N)]
    dp[0] = arr[0]

    for m in range(3):
        if m == k:
            dp[1][m] = int(1e9)
        else:
            dp[1][m] = dp[0][k] + arr[1][m]

    for i in range(2, N):
        for j in range(3):
            dp[i][j] = min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3]) + arr[i][j]

    for n in range(3):
        if n == k:
            continue
        if dp[N-1][n] < result:
            result = dp[N-1][n]

print(result)