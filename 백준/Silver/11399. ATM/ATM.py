N = int(input())
times = sorted(list(map(int, input().split())))
result = 0

tmp = 0
for i in times:
    tmp += i
    result += tmp
print(result)