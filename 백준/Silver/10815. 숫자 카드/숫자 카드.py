import sys

N = int(input())
h_lst = list(map(float, sys.stdin.readline().split()))
have = sorted(h_lst)
M = int(input())
c_lst = list(map(float, sys.stdin.readline().split()))

for c in c_lst:
    start = 0
    end = N-1

    while True:
        middle = (start + end) // 2
        if c == have[middle]:
            print(1, end=' ')
            break
        elif c < have[middle]:
            end = middle - 1
        elif c > have[middle]:
            start = middle + 1

        if start > end:
            print(0, end=' ')
            break