L = int(input())
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
cake = [0 for _ in range(L+1)]

expect = 0
for i in range(N):
    a, b = lst[i]
    if (b-a) > expect:
        expect = b-a
        expect_idx = i+1
print(expect_idx)

real = 0
for j in range(N):
    cnt = 0
    for k in range(lst[j][0], lst[j][1]+1):
        if cake[k] == 0:
            cake[k] = 1
            cnt += 1
    if cnt > real:
        real = cnt
        real_idx = j + 1
print(real_idx)