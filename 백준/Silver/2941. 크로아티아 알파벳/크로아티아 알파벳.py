string = input()
cnt = 0
ca_lst = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

while string:
    if string[0:3] == 'dz=':
        cnt += 1
        string = string.replace(string[0:3], '', 1)

    elif string[0:2] in ca_lst:
        cnt += 1
        string = string.replace(string[0:2], '', 1)

    else:
        cnt += 1
        string = string.replace(string[0], '', 1)

print(cnt)