import sys
from collections import deque

N, M = map(int, input().split())
parking_fee = {}        
car_weight = {}
parking = [[0] for _ in range(N)]
q = deque()
result = 0

for n in range(N):
    parking_fee[n] = int(input())
for m in range(M):
    car_weight[m] = int(input())

for i in range(2*M):
    x = int(input())

    if x > 0:
        cnt = 0
        for p in range(N):
            if parking[p][0] == 0:
                parking[p][0] += x
                result += (parking_fee[p] * car_weight[x-1])
                break
            else:
                cnt += 1
        if cnt == N:
            q.append(x)

    else:
        x = abs(x)
        for i in range(N):
            if parking[i][0] == x:
                x_idx = i
                parking[x_idx][0] = 0

                if q:
                    pop_num = q.popleft()
                    parking[x_idx][0] += pop_num
                    result += (parking_fee[x_idx] * car_weight[pop_num-1])

print(result)
