N = int(input())
lst = [list(input().split()) for _ in range(N)]
lst.sort(key=lambda x:int(x[0]))
for l in lst:
    print(*l)