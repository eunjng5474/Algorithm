while True:
    nums = sorted(list(map(int, input().split())))
    a = nums[0]
    b = nums[1]
    c = nums[2]
    if a == b == c == 0:
        break

    if a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')