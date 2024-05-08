import sys
input = sys.stdin.readline

def eat(arr):
    global answer
    for i in range(n):
        row_cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                row_cnt += 1
            else:
                row_cnt = 1
            answer = max(answer, row_cnt)

        col_cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
                col_cnt += 1
            else:
                col_cnt = 1
            answer = max(answer, col_cnt)


def change(arr):
    for i in range(n):
        for j in range(n-1):
            if arr[i][j] != arr[i][j+1]:
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
                eat(arr)
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            if arr[j][i] != arr[j+1][i]:
                arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
                eat(arr)
                arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]

n = int(input())
arr = [list(input()) for _ in range(n)]
answer = 1
change(arr)
print(answer)