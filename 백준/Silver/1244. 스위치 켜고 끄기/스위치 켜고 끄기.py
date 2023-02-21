import sys

n_sw = int(input())
switch = list(map(int, sys.stdin.readline().split()))
n_st = int(input())
for n in range(n_st):
    gender, num = map(int, sys.stdin.readline().split())
    num_idx = num - 1
    if gender == 1:
        for i in range(num_idx, n_sw, num):
            if switch[i] == 0:
                switch[i] = 1
            else:
                switch[i] = 0
    else:
        x, y = num_idx, num_idx
        while True: 
            if 0 <= x-1 < n_sw and 0 <= y+1 < n_sw:
                if switch[x-1] == switch[y+1]:
                    x, y = x-1, y+1
                else:
                    break
            else:
                break
        for j in range(x, y+1):
            if switch[j] == 0:
                switch[j] = 1
            else:
                switch[j] = 0

for i in range(n_sw):
    print(switch[i], end=' ')
    if i % 20 == 19:
        print()