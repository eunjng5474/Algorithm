import sys

inp_lst = [int(sys.stdin.readline().rstrip()) for _ in range(9)]
lst = sorted(inp_lst)
tmp = 0

for i in range(8):
    for j in range(i+1, 9):
        if sum(lst) - lst[i] - lst[j] == 100:
            a, b = lst[i], lst[j]
            lst.remove(a)
            lst.remove(b)
            tmp = 1
            break
    if tmp == 1:
        break

for r in lst:
    print(r)