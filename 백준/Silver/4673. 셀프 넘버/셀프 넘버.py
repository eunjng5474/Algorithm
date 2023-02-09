def d(n):
    nl = len(str(n))
    res_n = n
    for i in range(nl):
        res_n += int(str(n)[i])
    return res_n

non_self_num_lst = []
for i in range(1, 10001):
    result_i = d(i)
    non_self_num_lst.append(result_i)

for j in range(1, 10001):
    if j not in non_self_num_lst:
        print(j)