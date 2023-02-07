T = int(input())

for tc in range(T):
    H, W, N = map(int, input().split())

    floor = N % H
    num = (N // H) + 1
    if floor == 0:
        floor = H
        num = N // H
    result = floor * 100 + num
    print(result)