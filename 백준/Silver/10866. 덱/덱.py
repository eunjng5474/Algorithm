from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque()
for n in range(N):
    string = input().split()

    if string[0] == "push_front":
        q.appendleft(int(string[1]))

    if string[0] == "push_back":
        q.append(int(string[1]))

    if string[0] == "pop_front":
        if q:
            print(q.popleft())
        else:
            print(-1)

    if string[0] == "pop_back":
        if q:
            print(q.pop())
        else:
            print(-1)

    if string[0] == "size":
        print(len(q))

    if string[0] == "empty":
        if q:
            print(0)
        else:
            print(1)

    if string[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)

    if string[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)