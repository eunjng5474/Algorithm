import sys

N, K = map(int, input().split())
lst = list(map(int, sys.stdin.readline().split()))

result = []
tmp = sum(lst[:K])
result.append(tmp)
for i in range(1, N-K+1):
    sum_n = result[-1] - lst[i-1] + lst[i+K-1]
    result.append(sum_n)

print(max(result))
