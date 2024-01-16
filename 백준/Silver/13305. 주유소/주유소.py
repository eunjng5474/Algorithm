import sys
input = sys.stdin.readline

n = int(input().rstrip())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

result = 0
min_price = prices[0]

for i in range(n-1):
    min_price = min(min_price, prices[i])
    result += min_price * roads[i]

print(result)