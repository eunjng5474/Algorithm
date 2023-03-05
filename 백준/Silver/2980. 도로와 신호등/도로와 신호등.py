N, L = map(int, input().split())
time = 0

lst = [[0] * 3] + [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N+1):
    time += lst[i][0] - lst[i-1][0]     # 다음 신호등까지 가는 데 걸리는 시간
    time += max(0, lst[i][1] - (time % (lst[i][1] + lst[i][2])))
    # R + G가 신호등 주기이고, R - (time % (R+G))가 대기시간. 만약 음수면 대기 없이 바로 지나감 => 0 더하기
time += (L - lst[-1][0])                # 마지막 신호등부터 도로 끝까지 가는 데 걸리는 시간 
print(time)