import sys
from collections import deque

n, w, L = map(int, input().split())
weight = deque(map(int, sys.stdin.readline().split()))
bridge = deque()
for i in range(w-1):
    bridge.append(0)
bridge.append(weight[0])
weight.popleft()
time = 1

while True:
    bridge.popleft()
    if weight and sum(bridge) + weight[0] <= L:
        bridge.append(weight.popleft())
    else:
        bridge.append(0)
    time += 1
    
    if not weight and sum(bridge) == 0:
        break

print(time)