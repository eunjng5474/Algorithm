C = int(input())
for tc in range(C):
    d, n = map(int, input().split())
    nums = list(map(int, input().split()))
    cnt = 0

    mod = [0] * d
    sum_n = 0

    for num in nums:
        sum_n += num
        sum_n = sum_n % d

        cnt += mod[sum_n]
        mod[sum_n] += 1

    cnt += mod[0]
    print(cnt)