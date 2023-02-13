import sys

N = int(input())
stack = []

for n in range(N):
    string = list(sys.stdin.readline().split())
    # print(string)

    if string[0] == 'push':
        stack.append(int(string[1]))
    
    elif string[0] == 'pop':
        try:
            result = stack.pop()
            print(result)
        except:
            print(-1)
    
    elif string[0] == 'size':
        print(len(stack))
    
    elif string[0] == 'empty':
        if stack:
            result = 0
        else:
            result = 1
        print(result)
    
    elif string[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)