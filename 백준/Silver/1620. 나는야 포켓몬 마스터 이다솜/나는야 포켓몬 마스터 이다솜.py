import sys

n, m = map(int, input().split())
int_dic = {}
name_dic = {}
for i in range(1, n+1):
    n_in = sys.stdin.readline().rstrip()
    int_dic[i] = n_in
    name_dic[n_in] = i

for j in range(m):
    a = sys.stdin.readline().rstrip()
    if a.isdigit() == True:
        print(int_dic[int(a)])
    else:
        print(name_dic[a])
