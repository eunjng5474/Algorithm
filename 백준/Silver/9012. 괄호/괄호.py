T = int(input())

for tc in range(T):
    ps = input()
    stack = []
    
    for n in ps:
        if n == '(':
            stack.append(n)
        elif n == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(n)
                break
    
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')