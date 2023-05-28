import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().rstrip().split()))
sets = set(numbers)

nums = list(sets)
nums.sort()
dic = {}

i = 0
for n in nums:
    dic[n] = i
    i += 1

for n in numbers:
    print(dic[n], end=" ")