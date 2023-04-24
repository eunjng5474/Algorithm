def sol(col, tmp):
    global result
    if col == 11:
        result = max(result, tmp)
        return

    for i in range(11):
        if arr[col][i] == 0:
            continue

        if not used[i]:
            used[i] = 1
            sol(col+1, tmp+arr[col][i])
            used[i] = 0


C = int(input())
for tc in range(C):
    arr = [list(map(int, input().split())) for _ in range(11)]
    result = 0
    used = [0] * 11
    sol(0, 0)
    print(result)