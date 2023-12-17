import sys
input = sys.stdin.readline

def sol(a, b, c):
    if b == 1:
        return a % c

    n = sol(a, b//2, c)
    if b % 2:
        return n**2 * a % c
    else:
        return n**2 % c

a, b, c = map(int, input().split())
print(sol(a, b, c))