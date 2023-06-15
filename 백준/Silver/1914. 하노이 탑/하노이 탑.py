def hanoi(n, start, end, tmp):
    global result, k
    if n == 1:
        print(start, end)
        return
    
    hanoi(n-1, start, tmp, end)
    print(start, end)
    hanoi(n-1, tmp, end, start)

n = int(input())
print(2**n - 1)
if n <= 20:
    hanoi(n, 1, 3, 2)