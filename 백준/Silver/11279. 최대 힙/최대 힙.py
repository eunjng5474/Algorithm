import heapq
import sys

hq = []
N = int(input())
for n in range(N):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(hq, -x)
    else:
        if not hq:
            print(0)
        else:
            print(-heapq.heappop(hq))
