import sys

N, K = map(int, input().split())
student = [[0, 0] for _ in range(6)]
result = 0

for n in range(N):
    s, y = map(int, sys.stdin.readline().split())
    student[y-1][s] += 1

for i in student:
    for j in i:
        if j > K:
            result += (j // K + 1)
        elif j != 0:
            result += 1

print(result)
