
def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    for x, y in puddles:
        dp[y][x] = -1   # x, y 반대

    for i in range(1, n+1):
        for j in range(1, m+1):
            # -1이면 물에 잠긴 지역이므로 contiune
            if dp[i][j] == -1:
                continue
            
            # 이전 위치의 값이 -1이면 0으로 계산
            cnt1 = max(0, dp[i-1][j])
            cnt2 = max(0, dp[i][j-1])
            dp[i][j] += (cnt1 + cnt2) % 1000000007
    
    return dp[n][m]