mushroom = [int(input()) for _ in range(10)]
result = 0
for m in mushroom:
    if result + m > 100:
        if ((result+m) - 100) <= (100-result):
            result += m
            break
        else:
            break
    result += m
    if result == 100:
        break

print(result)