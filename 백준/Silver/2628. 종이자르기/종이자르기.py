import sys

row_lst = [0] + []
col_lst = [0] + []
r, c = map(int, input().split())
line = int(input())
for l in range(line):
    d, n = map(int, sys.stdin.readline().split())
    if d == 0:              # 0이면 col_lst에 n 추가
        col_lst.append(n)
    else:                   # 1이면 row_lst
        row_lst.append(n)

col_lst.append(c)       # 리스트 앞뒤로 0과 해당 길이 추가 
row_lst.append(r)

col = sorted(col_lst)   ## [0, 2, 3, 8]
row = sorted(row_lst)   ## [0, 4, 10]

max_c = 0
max_r = 0

# 본인에서 본인 앞자리 숫자를 빼면 해당 칸 수가 됨
for i in range(1, len(col)):
    if (col[i] - col[i-1]) > max_c:
        max_c = col[i] - col[i-1]
for j in range(1, len(row)):
    if (row[j] - row[j-1]) > max_r:
        max_r = row[j] - row[j-1]

print(max_r * max_c)