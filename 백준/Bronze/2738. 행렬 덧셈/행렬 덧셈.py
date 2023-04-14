N, M = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(N)]
arr2 = [list(map(int, input().split())) for _ in range(N)]
result = [[0]* M for _ in range(N)]

for n in range(N):
    for m in range(M):
        result[n][m] = arr1[n][m] + arr2[n][m]

for r in result:
    print(*r)