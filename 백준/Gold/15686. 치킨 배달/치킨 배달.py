N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []
lst = []
visited = []
result = 50*50

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append([i, j])

        if arr[i][j] == 2:
            chicken.append([i, j])
            visited.append([False])

def sol(n):
    global result
    if len(lst) == M:
        # print(lst)
        tmp_sum = 0
        for h in house:
            tmp = 50 * 50
            for c in lst:
            # for h in house:
                distance = abs(h[0] - c[0]) + abs(h[1] - c[1])
                if distance < tmp:
                    tmp = distance
            tmp_sum += tmp
        # print(tmp_sum)
        if tmp_sum < result:
            result = tmp_sum
        return

    else:
        for i in range(n, len(chicken)):
            # if not visited[i]:
            lst.append(chicken[i])
            # visited[i] = True
            sol(i+1)
            lst.pop()
            # visited[i] = False

sol(0)
print(result)