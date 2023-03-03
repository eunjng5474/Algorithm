N = int(input())
i = 1
cnt = 1
while i < N:
    i += 6 * cnt
    cnt += 1
print(cnt)
