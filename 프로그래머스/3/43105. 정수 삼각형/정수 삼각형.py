def solution(triangle):
    answer = 0
    dp = triangle
    n = len(triangle)
    
    for i in range(1, n):
        for j in range(len(triangle[i])):
            if not j:
                dp[i][j] += dp[i-1][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])
            
            if dp[i][j] > answer:
                answer = dp[i][j]
                
    return answer