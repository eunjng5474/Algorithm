N = int(input())
num_lst = []
stack = []

result_lst = []
pop_lst = []
for i in range(N):
    num_lst.append(int(input()))

ver_num = 0
for n in num_lst:
    if n >= ver_num:
        for i in range(ver_num+1, n+1):
            stack.append(i)
            result_lst.append('+')
        p = stack.pop()
        pop_lst.append(p)
        result_lst.append('-')
        ver_num = n
    else:
        p = stack.pop()
        pop_lst.append(p)
        result_lst.append('-')

if num_lst != pop_lst:
    print('NO')
else:
    for r in result_lst:
        print(r)