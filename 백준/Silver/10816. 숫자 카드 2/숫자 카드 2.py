import sys
input = sys.stdin.readline

N = int(input())
have = sorted(list(map(int, input().split())))
M = int(input())
chk = list(map(int, input().split()))
cnt = {}
for h in have:
    if h in cnt:
        cnt[h] += 1
    else:
        cnt[h] = 1


for c in chk:
    start = 0
    end = N - 1

    while True:
        middle = (start + end) // 2
        if have[middle] == c:
            print(cnt[c], end=' ')
            break
        elif have[middle] > c:
            end = middle - 1
        elif have[middle] < c:
            start = middle + 1

        if start > end:
            print(0, end=' ')
            break