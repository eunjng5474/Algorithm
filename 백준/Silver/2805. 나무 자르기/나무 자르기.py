import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree)

while start <= end:
    mid = (start + end) // 2
    rest = 0

    for t in tree:
        if t > mid:
            rest += (t - mid)
    if rest >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)