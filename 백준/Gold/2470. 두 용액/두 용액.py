import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(list(map(int, input().split())))
a, b = 0, 0
value = 2000000000

i = 0
j = len(lst) - 1
while j > i:
    tmp = lst[i] + lst[j]
    if abs(tmp) < value:
        value = abs(tmp)
        a, b = lst[i], lst[j]
        if tmp == 0:
            break

    if tmp < 0:
        i += 1
    elif tmp > 0:
        j -= 1

print(a, b)