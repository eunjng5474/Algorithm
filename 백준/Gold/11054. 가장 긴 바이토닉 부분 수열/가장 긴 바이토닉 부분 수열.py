import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
inc = [1 for _ in range(n)]
dec = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            inc[i] = max(inc[i], inc[j] + 1)
    for k in range(n-1, n-i-1, -1):
        if nums[n-i-1] > nums[k]:
            dec[n-i-1] = max(dec[n-i-1], dec[k] + 1)

result = 0
for i in range(n):
    result = max(result, inc[i] + dec[i])

print(result - 1)