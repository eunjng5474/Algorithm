n, b = map(int, input().split())
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = ''

while n:
    result += num[n%b]
    n //= b

print(result[::-1])