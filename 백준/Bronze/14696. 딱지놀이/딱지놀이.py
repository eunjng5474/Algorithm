N = int(input())

def play(a, b):
    if a.count(4) > b.count(4):
        return 'A'
    elif a.count(4) < b.count(4):
        return 'B'

    if a.count(3) > b.count(3):
        return 'A'
    elif a.count(3) < b.count(3):
        return 'B'

    if a.count(2) > b.count(2):
        return 'A'
    elif a.count(2) < b.count(2):
        return 'B'

    if a.count(1) > b.count(1):
        return 'A'
    elif a.count(1) < b.count(1):
        return 'B'
    else:
        return 'D'


for n in range(N):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(play(a[1:], b[1:]))
