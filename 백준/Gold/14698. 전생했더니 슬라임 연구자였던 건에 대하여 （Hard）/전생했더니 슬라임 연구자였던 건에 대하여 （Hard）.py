import sys
input = sys.stdin.readline
import heapq

T = int(input())
for tc in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    if N == 1:
        print(1)
        continue

    result = 1
    hq = []
    for n in nums:
        heapq.heappush(hq, n)

    while True:
        if len(hq) == 1:
            break
        # 작은 값 두 개 pop해서 곱한 뒤 다시 추가 
        energy = heapq.heappop(hq)*heapq.heappop(hq)
        result *= energy
        heapq.heappush(hq, energy)
    print(result % 1000000007)