import sys
input = sys.stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    tmp = input().rstrip()[1:-1].split(",")
    q = deque(tmp)
    if not n:
        q = deque()

    cnt = 0
    flag = False
    for i in p:
        if i == "R":
            # q.reverse()
            cnt += 1
        else:
            if q:
                # 현재까지 뒤집는 횟수가 홀수면 뒤집어서 popleft => pop()
                # 짝수면 안 뒤집어도 됨 => popleft()
                if cnt % 2:
                    q.pop()
                else:
                    q.popleft()
            else:
                print("error")
                flag = True
                break
    if flag:
        continue

    # R 횟수가 홀수면 뒤집기 
    if cnt % 2:
        q.reverse()

    result = "["
    result += ",".join(list(q))
    result += "]"
    print(result)