import sys
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    clothes = {}
    n = int(input())
    cnt = 1
    for _ in range(n):
        name, type = input().split()
        if type in clothes:
            clothes[type].append(name)
        else:
            clothes[type] = [name]

    for i in clothes:
        cnt *= len(clothes[i])+1
    print(cnt - 1)