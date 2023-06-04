import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
cnt = 0

for x in range(N):
    one, two = 0, 0
    visited = [0 for _ in range(M)]
    for y in range(M):
        if arr[x][y] == 1 and not visited[y]:
            visited[y] = 1
            one += 1
            for k in range(1, M):
                if y + k < M and arr[x][y + k] == 1 and not visited[y + k]:
                    visited[y + k] = 1
                else:
                    break


        if arr[x][y] == 2 and not visited[y]:
            visited[y] = 2
            two += 1
            for k in range(1, M):
                if y + k < M and arr[x][y + k] == 2 and not visited[y + k]:
                    visited[y + k] = 2
                else:
                    break
        if not arr[x][y]:
            if not one and not two:
                continue
            cnt += (min(one, two) + 1)
            one, two = 0, 0
    if not one and not two:
        continue
    cnt += (min(one, two) + 1)
print(cnt)