N, M, L = map(int, input().split())
cnt = 0     # 공 던지는 횟수
people = [0 for _ in range(N+1)]

idx = 1
people[1] += 1
while True:
    if people[idx] == M:
        break
    if (people[idx]) % 2:
        idx = (idx+L) % N
        people[idx] += 1
    else:
        idx = (idx-L) % N
        people[idx] += 1
    cnt += 1

print(cnt)