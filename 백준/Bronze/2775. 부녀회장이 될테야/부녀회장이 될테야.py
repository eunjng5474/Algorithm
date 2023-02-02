t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    k_li = []
    
    for j in range(1, n+1):
        k_li.append(j)

    for l in range(k):
        for m in range(1, n):
            k_li[m] += k_li[m-1]

    print(k_li[-1])