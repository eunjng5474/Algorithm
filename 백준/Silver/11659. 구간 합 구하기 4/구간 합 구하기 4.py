import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
sums = [0] * (N+1)
for i in range(N):
    sums[i+1] = sums[i] + nums[i]
# print(sums)

for m in range(M):
    i, j = map(int, input().split())
    print(sums[j] - sums[i-1])