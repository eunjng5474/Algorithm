import sys
input = sys.stdin.readline

N = int(input())
nums = list(int(input()) for _ in range(N))
nums.sort()
for n in nums:
    print(n)