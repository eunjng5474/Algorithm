from collections import deque

T = int(input())

for tc in range(T):
    queue = deque()
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    result_lst = []

    for n in range(len(nums)):
        queue.append((n, nums[n]))
    
    while queue:
        max_n = queue[0][1]
        for i in queue:
            if i[1] > max_n:
                max_n = i[1]
        x, y = queue.popleft()
        if y < max_n:
            queue.append((x, y))
        else:
            result_lst.append(x)
    
    result = result_lst.index(M) + 1
    print(result)
        