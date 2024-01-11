import sys
input = sys.stdin.readline

str = input().rstrip()
explosion = input().rstrip()

n = len(explosion)
stack = []

for i in range(len(str)):
    stack.append(str[i])
    if "".join(stack[-n:]) == explosion:
        for j in range(n):
            stack.pop()

if not stack:
    print("FRULA")
else:
    for s in stack:
        print(s, end="")