N = int(input())
lst = sorted([list(map(int, input().split())) for _ in range(N)])
result = 0

max_h = 0
for i in range(N):
    if lst[i][1] > max_h:
        max_h = lst[i][1]
        max_h_idx = lst[i][0]

tmp = [lst[0][0], lst[0][1]]
for i in range(1, N):
    if lst[i][1] >= tmp[1]:
        result += (lst[i][0] - tmp[0]) * tmp[1]
        tmp = [lst[i][0], lst[i][1]]
    if tmp[0] == max_h_idx:                # 최대 높이 기둥에 도달하면
        tmp = [lst[-1][0], lst[-1][1]]      # 뒤에서부터 조사하게 tmp를 마지막 기둥으로 변경
        break

for i in range(N-2, -1, -1):    # 마지막 기둥은 위에서 tmp로 기록했으니 N-2부터
    if lst[i][1] >= tmp[1]:
        result += (tmp[0] - lst[i][0]) * tmp[1]
        tmp = [lst[i][0], lst[i][1]]
    if tmp[0] == max_h_idx:
        break

result += max_h
print(result)