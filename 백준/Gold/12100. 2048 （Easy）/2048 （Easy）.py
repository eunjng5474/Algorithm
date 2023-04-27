from copy import deepcopy
import sys
input = sys.stdin.readline

N = int(input())
input_arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

def move(arr, d):
    if d == 0:      # 상
        for j in range(N):  # 열
            end = 0         # 가장 윗줄 == 끝
            for i in range(1, N):   # 1행 ~
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if not arr[end][j]:  # 0이면 끝으로 옮기기
                        arr[end][j] = tmp
                    elif arr[end][j] == tmp:  # 같으면 *2
                        arr[end][j] *= 2
                        end += 1
                    else:
                        end += 1                # 다르면 end += 1 해서 값 옮기기
                        arr[end][j] = tmp
                    # arr[i][j] = 0
                    #### arr[i][j]를 end 이용한 위치에 넣고 이후에 0으로 바꾸면 답 안 나옴,,,,

    if d == 1:      # 하
        for j in range(N):
            end = N-1
            for i in range(N-2, -1, -1):  # 밑(end 윗줄)에서부터 위로
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if not arr[end][j]:
                        arr[end][j] = tmp
                    elif arr[end][j] == tmp:
                        arr[end][j] *= 2
                        end -= 1
                    else:
                        end -= 1
                        arr[end][j] = tmp

    if d == 2:      # 좌
        for i in range(N):  # 행
            end = 0
            for j in range(1, N):  # 1열 ~
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if not arr[i][end]:
                        arr[i][end] = tmp
                    elif arr[i][end] == tmp:
                        arr[i][end] *= 2
                        end += 1
                    else:
                        end += 1
                        arr[i][end] = tmp

    if d == 3:      # 우
        for i in range(N):
            end = N-1
            for j in range(N-2, -1, -1):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if not arr[i][end]:
                        arr[i][end] = tmp
                    elif arr[i][end] == tmp:
                        arr[i][end] *= 2
                        end -= 1
                    else:
                        end -= 1
                        arr[i][end] = tmp
    return arr


def dfs(arr, cnt):
    global result
    if cnt == 5:
        for n in range(N):
            result = max(result, max(arr[n]))
        return

    for d in range(4):
        tmp_arr = move(deepcopy(arr), d)
        dfs(tmp_arr, cnt+1)


dfs(input_arr, 0)
print(result)