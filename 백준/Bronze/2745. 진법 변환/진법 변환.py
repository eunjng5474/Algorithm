n, b = input().split()
n = n[::-1]
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = 0

for i in range(len(n)):
    result += num.index(n[i]) * (int(b)**i)

print(result)