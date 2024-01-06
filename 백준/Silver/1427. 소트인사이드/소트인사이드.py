import sys
input = sys.stdin.readline

num = list(map(int, input().rstrip()))
num.sort(reverse=True)
for n in num:
    print(n, end="")