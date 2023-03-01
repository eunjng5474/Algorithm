import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(5)]
call = []
for n in range(5):
    a, b, c, d, e = map(int, input().split())
    call.append(a)
    call.append(b)
    call.append(c)
    call.append(d)
    call.append(e)

for c in range(25):
    result = 0
    for i in range(5):
        for j in range(5):
            if arr[i][j] == call[c]:
                arr[i][j] = 0
    if c >= 4:
        tmp_cross1 = 0
        tmp_cross2 = 0
        for k in range(5):
            if sum(arr[k]) == 0:
                result += 1
            tmp_cross1 += arr[k][k]
            tmp_cross2 += arr[k][4-k]
        if tmp_cross1 == 0:
            result += 1
        if tmp_cross2 == 0:
            result += 1

        for k in range(5):
            tmp_col = 0
            for l in range(5):
                tmp_col += arr[l][k]
            if tmp_col == 0:
                result += 1

    if result >= 3:
        print(c+1)
        break