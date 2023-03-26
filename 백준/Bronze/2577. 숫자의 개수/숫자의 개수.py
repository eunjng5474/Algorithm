num = 1
for tc in range(3):
    num *= int(input())
num_str = str(num)

lst = [0] * 10
for n in num_str:
    lst[int(n)] += 1
for l in lst:
    print(l)