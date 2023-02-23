import sys
import heapq

hq = []
N = int(input())
for n in range(N):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(hq, (abs(x), x))
    else:
        if hq:
            a, b = heapq.heappop(hq)
            print(b)
        else:
            print(0)