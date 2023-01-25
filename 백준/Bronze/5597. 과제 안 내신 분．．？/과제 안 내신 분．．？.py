x_list = []
for i in range(28):
    x_list.append(int(input()))
# print(x_list)
x_list = sorted(x_list)
# print(x_list)
for j in range(1, 31):
    if j not in x_list:
        print(j)