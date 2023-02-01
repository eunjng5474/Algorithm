n = int(input())

a = b = 0
for i in range((n//3)+1, 0, -1):
    if n - (5*i) == 0:
        b = n // 5
        print(b)
        break
    elif (n - (5*i)) > 0 and (n - (5*i)) % 3 == 0:
        a = (n - (5*i)) // 3
        b = a + i
        print(b)
        break
if not b and n % 3 == 0:
    b = n // 3
    print(b)
elif not b:
    print(-1)