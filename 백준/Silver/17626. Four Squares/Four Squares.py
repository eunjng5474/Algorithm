n = int(input())
dp = [0, 1]
for i in range(2, n+1):
    num = 4 # 최소값 -> 모든 수 4개 이하의 제곱 수로 나타낼 수 있음
    j = 1
    while i >= j**2:
        num = min(num, dp[i-j**2])
        j += 1
    
    dp.append(num+1)  # 최소값 + 1회

print(dp[n])