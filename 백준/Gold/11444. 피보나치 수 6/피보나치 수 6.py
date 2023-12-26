import sys
input = sys.stdin.readline

def mul(a, b):  # 행렬 곱셈
    res = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += a[i][k] * b[k][j] % 1000000007
    return res

def sol(a, b):  # 분할 정복
    if b == 1: return a
    else:
        tmp = sol(a, b//2)
        if not b % 2:
            return mul(tmp, tmp)
        else:
            return mul(mul(tmp, tmp), a)


n = int(input())
matrix = [[1, 1], [1, 0]]
result = sol(matrix, n)
print(result[0][1] % 1000000007)