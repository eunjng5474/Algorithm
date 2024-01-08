def dfs(num, cnt):
    global result
    if num == b:
        result = min(result, cnt)
        return
    if cnt >= result or num > b:
        return

    dfs(num * 2, cnt+1)
    tmp = int(str(num) + "1")
    dfs(tmp, cnt+1)

a, b = map(int, input().split())
result = int(1e9)
dfs(a, 0)
if result == int(1e9):
    print(-1)
else:
    print(result + 1)