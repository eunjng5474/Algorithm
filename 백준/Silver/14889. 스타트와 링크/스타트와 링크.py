import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
people = [i for i in range(N)]
visited = [0] * N
start_lst = []
result = 100 * N * N

def start_sum(lst):
    start = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            start += arr[lst[i]][lst[j]]
            start += arr[lst[j]][lst[i]]

    return start

def link_sum(lst):
    link = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            link += arr[lst[i]][lst[j]]
            link += arr[lst[j]][lst[i]]

    return link


def sol(n):
    global result
    if len(start_lst) == N//2:
        link_lst = []
        start = start_sum(start_lst)

        for p in people:
            if p not in start_lst:
                link_lst.append(p)
        link = link_sum(link_lst)

        if abs(start - link) < result:
            result = abs(start - link)

        return

    for i in range(n, N):
        start_lst.append(i)
        sol(i+1)
        start_lst.pop()

sol(0)
print(result)