import sys
input = sys.stdin.readline
from collections import deque
# import copy, time

N, M = map(int, input().split())
# start_time = time.time()

arr = [list(map(int, input().split())) for _ in range(N)]
# lst = [[0] * M for _ in range(N)]
result = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def add_wall(wall):     # 벽 3개 추가할 때마다 bfs로 확인
    if wall == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if not arr[i][j]:
                arr[i][j] = 1
                add_wall(wall+1)    # 벽을 세울 수 있는 모든 위치에 놓아봄
                arr[i][j] = 0


def bfs():
    global result

    lst = []
    for a in arr:
        lst.append(list(a))     # 원본 변형 막기 위해 lst라는 새로운 배열로 복사

    q = deque()
    for n in range(N):
        for m in range(M):
            if lst[n][m] == 2:      # 바이러스 위치 모두 q에 저장
                q.append((n, m))
                # lst[n][m] = 2

    while q:                        # bfs 사용해서 바이러스 다 퍼지게 만들기
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if not lst[nx][ny]:
                    lst[nx][ny] = 2
                    q.append((nx, ny))

    cnt = 0                     # while문이 종료되면(q에 값 없으면) 모든 바이러스가 퍼진 상황
    for i in range(N):
        cnt += lst[i].count(0)
        # for j in range(M):
        #     if lst[i][j] == 0:  # 이 때 0의 개수 세기
        #         cnt += 1

    if cnt > result:
        result = cnt

add_wall(0)
print(result)