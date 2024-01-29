import sys
input = sys.stdin.readline

def cal(matrix1, matrix2):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += matrix1[i][k] * matrix2[k][j] % 1000
    return res

def sol(a, b):
    if b == 1:
        return a
    else:
        tmp = sol(a, b//2)
        if b % 2:
            return cal(cal(tmp, tmp), a)
        else:
            return cal(tmp, tmp)

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
res = sol(matrix, b)

for i in range(n):
    for j in range(n):
        print(res[i][j] % 1000, end=" ")
    print()