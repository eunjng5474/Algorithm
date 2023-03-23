music = list(x for x in range(1, 9))
nums = list(map(int, input().split()))

if nums == music:
    print('ascending')
elif nums == music[::-1]:
    print('descending')
else:
    print('mixed')