import sys
input = sys.stdin.readline
import heapq

hq = []

N = int(input())
for n in range(N):
    x = int(input())
    
    if x == 0:
        if len(hq):
            print(heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq, x)