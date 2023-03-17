N = int(input())
times = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:(x[1], x[0]))
result = 0

tmp = [0, 0]
for n in range(N):
    if times[n][0] >= tmp[1]:
        result += 1
        tmp = times[n]
print(result)