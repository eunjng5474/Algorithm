n = int(input())
result = n
for i in range(2, n):
    for j in range(i, n//i+1):
        result += 1
print(result)