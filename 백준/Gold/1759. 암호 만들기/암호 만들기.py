import sys
input = sys.stdin.readline

def check(lst):
    v = 0
    c = 0
    for i in lst:
        if i in 'aeiou':
            v += 1
        else:
            c += 1
    if v >= 1 and c >= 2:
        return True
    else:
        return False

def sol(n):
    if len(lst) == L:
        flag = check(lst)
        if not flag:
            return

        for l in lst:
            print(l, end='')
        print()
        return

    for i in range(n, C):
        lst.append(alphabet[i])
        sol(i+1)
        lst.pop()


L, C = map(int, input().split())
alphabet = sorted(list(input().split()))
lst = []
sol(0)