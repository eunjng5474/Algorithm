import sys
from collections import deque

N = int(input())
queue = deque()
for n in range(N):
    string = sys.stdin.readline().rstrip().split()

    if string[0] == 'push':
        queue.append(string[1])
    
    elif string[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    
    elif string[0] == 'size':
        print(len(queue))
    
    elif string[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
        
    elif string[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    
    elif string[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])