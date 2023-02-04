n = int(input())

n_li = list(map(int, input().split()))
cnt = len(n_li)

for i in n_li:
    if i == 1:
        cnt -= 1
    else:
        for j in range(2, i):
            if i % j == 0:
                cnt -= 1

                break
print(cnt)