import sys
input = sys.stdin.readline

n = int(input())
dic = dict()
for _ in range(n):
    name, log = input().split()
    if log == 'enter':
        dic[name] = True
    else:
        del dic[name]

result = sorted(dic.keys(), reverse=True)
for i in result:
    print(i)