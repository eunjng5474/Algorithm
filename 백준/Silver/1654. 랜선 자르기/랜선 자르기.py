import sys
input = sys.stdin.readline

K, N = map(int, input().split())
nums = [int(input()) for _ in range(K)]
start, end = 1, max(nums)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for n in nums:
        cnt += n // mid

    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)  # 최종적인 end가 랜선 최대 길이가 됨