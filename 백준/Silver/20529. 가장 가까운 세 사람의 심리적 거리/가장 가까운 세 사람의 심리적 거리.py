import sys, itertools
input = sys.stdin.readline

def check(lst):
    cnt = 0
    if lst[0] == lst[1] == lst[2]:
        return 0
    for i in range(4):
        if lst[0][i] != lst[1][i]:
            cnt += 1
        if lst[0][i] != lst[2][i]:
            cnt += 1
        if lst[2][i] != lst[1][i]:
            cnt += 1
    return cnt


t = int(input())
for _ in range(t):
    n = int(input())
    mbti = input().split()
    result = 1e9

    if n > 32:
        print(0)
        continue

    for c in itertools.combinations(mbti, 3):
        cnt = check(c)
        result = min(cnt, result)
    print(result)