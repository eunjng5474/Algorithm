import sys
input = sys.stdin.readline

N = int(input())
arr = []
for n in range(N):
    a, b, c = map(int, input().split())
    arr.append([[a, 1], [b, 2], [c, 3]])
    # 비용과 색깔 저장(R = 1, G = 2, B = 3)

result = int(1e9)

for k in range(3):
    dp = [[[0, 0] for i in range(3)] for _ in range(N)]
    dp[0] = arr[0]


    for m in range(3):
        if m == k:
            dp[1][m][0] = int(1e9)
        else:
            dp[1][m][0] = dp[0][k][0] + arr[1][m][0]
            dp[1][m][1] = k+1

    for i in range(2, N):
        for j in range(3):
            if dp[i-1][(j+1)%3][0] < dp[i-1][(j+2)%3][0]:
                dp[i][j][0] = dp[i-1][(j+1)%3][0] + arr[i][j][0]
                dp[i][j][1] = dp[i-1][(j+1)%3][1]
            else:
                dp[i][j][0] = dp[i-1][(j+2)%3][0] + arr[i][j][0]
                dp[i][j][1] = dp[i-1][(j+2)%3][1]

    for n in range(3):
        if n+1 == dp[N-1][n][1]:
            continue
        if dp[N-1][n][0] < result:
            result = dp[N-1][n][0]

print(result)