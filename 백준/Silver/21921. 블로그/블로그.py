import sys
input = sys.stdin.readline

n, x = map(int, input().split())
nums = list(map(int, input().split()))

tmp = sum(nums[:x])
answer = tmp
cnt = 1

for i in range(1, n-x+1):
    tmp -= nums[i - 1]
    tmp += nums[i + x - 1]

    if tmp == answer:
        cnt += 1
    if tmp > answer:
        answer = tmp
        cnt = 1

if answer == 0:
    print("SAD")
else:
    print(answer)
    print(cnt)