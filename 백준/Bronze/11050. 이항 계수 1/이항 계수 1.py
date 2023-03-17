N, K = map(int, input().split())
result = 1
for i in range(N, N-K, -1):
    result *= i
for j in range(K, 0, -1):
    result //= j

print(result)