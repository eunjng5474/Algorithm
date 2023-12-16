import sys
input = sys.stdin.readline

mid = input().strip()
result = ''
stack = []

for m in mid:
    if m == '(':
        stack.append(m)
    elif m == '*' or m == '/':
        while stack and stack[-1] in ['*', '/']:
            result += stack.pop()
        stack.append(m)
    elif m == '+' or m == '-':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(m)
    elif m == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()
    else:
        result += m

while stack:
    result += stack.pop()

print(result)