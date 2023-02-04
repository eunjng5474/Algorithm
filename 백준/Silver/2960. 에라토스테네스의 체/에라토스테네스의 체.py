n,k = map(int, input().split())
lst = list(range(2, n+1))
result_li = []

i = 1
while i <= n:
    p = lst.pop(0)
    result_li.append(p)

    for j in range(1, (n//p+1)):
        try:
            lst.remove(p * j)
            result_li.append(p * j)
        except:
            i += 1
    if not lst:
        break
        
print(result_li[k-1])   