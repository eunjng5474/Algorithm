dc_lst = []
N = int(input())
rank_lst = []

for n in range(N):
    w, h = map(int, input().split())
    dc_lst.append((w, h))

for i in dc_lst:
    rank = 1
    for j in dc_lst:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    rank_lst.append(rank)

print(*rank_lst)