import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

left = 0
right = 0
sum_n = 0
result = 1000000

while True:
    if sum_n >= S:
        result = min(result, right - left)
        # 합에서 left 인덱스의 수 뺀 후, 다음 인덱스부터 진행하도록
        sum_n -= nums[left]
        left += 1
    elif right == N:
        break

    else:
        sum_n += nums[right]
        right += 1

if result == 1000000:
    print(0)
else:
    print(result)