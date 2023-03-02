N = int(input())
result = []

for i in range(N+1):
    tmp = [N, i]
    num = N
    idx = 1
    while num >= 0:
        num = tmp[idx-1] - tmp[idx]
        if num >= 0:
            tmp.append(num)
        idx += 1

    if len(tmp) > len(result):
        result = tmp

print(len(result))
print(*result)