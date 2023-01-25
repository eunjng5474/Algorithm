x_list = []
for i in range(28):
    x_list.append(int(input()))
for j in range(1, 31):
    if j not in x_list:
        print(j)