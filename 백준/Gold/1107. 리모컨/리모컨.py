import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
if M != 0:
    nums = list(map(int, input().split()))
else:
    nums = []

minimum = abs(N - 100)

for i in range(1000001):
    num = str(i)

    for j in range(len(num)):
        if int(num[j]) in nums:
            break
        else:
            if j == len(num) - 1:
                cnt = abs(i - N) + len(num)
                if cnt < minimum:
                    minimum = cnt

print(minimum)