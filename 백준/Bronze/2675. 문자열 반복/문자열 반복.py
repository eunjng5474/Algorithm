T = int(input())
for tc in range(T):
    n, string = input().split()
    n = int(n)

    for s in string:
        print(s*n, end='')
    print()