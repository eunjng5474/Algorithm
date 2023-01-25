a_li = []
b_dic = {}
for i in range(10):
    a_li.append(int(input()))
for j in a_li:
    try:
        b_dic[j % 42] += 1
    except:
        b_dic[j % 42] = 1
print(len(b_dic))
