import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
result = N * M + 1

for i in range(N-7):
    for j in range(M-7):
        w_cnt = 0
        b_cnt = 0

        for a in range(i, i+8): # i부터 8칸까지
            for b in range(j, j+8):  # j부터 8칸까지
                if (a + b) % 2:      # a+b가 홀수이면
                    if arr[a][b] != 'B':
                        w_cnt += 1
                    else:
                        b_cnt += 1

                else:
                    if arr[a][b] != 'W':
                        w_cnt += 1
                    else:
                        b_cnt += 1
        result = min(w_cnt, b_cnt, result)
print(result)