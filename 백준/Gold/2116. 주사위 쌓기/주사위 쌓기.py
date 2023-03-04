import sys
input = sys.stdin.readline

def search(idx, bottom, num):
    global result
    while idx != N:
        bottom_idx = arr[idx].index(bottom)
        top_idx = opposite[bottom_idx]
        top = arr[idx][top_idx]

        tmp = list(arr[idx])
        tmp[bottom_idx] = 0
        tmp[top_idx] = 0
        num += max(tmp)
        bottom = top
        idx += 1
    if num > result:
        result = num


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
opposite = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}     # 마주보는 인덱스
result = 0

for i in range(6):
    search(0, arr[0][i], 0)
print(result)