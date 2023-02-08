def fib(n):
    cnt = 0
    if n == 1:
        cnt += 1
        return cnt
    elif n == 2:
        cnt += 1
        return cnt
    else:
        cnt += 1
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    fibo = [0] * (n+1)
    fibo[1] = 1
    fibo[2] = 1
    cnt = 0
    for i in range(3, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
        cnt += 1
    return cnt


n = int(input())
result1 = fib(n)
result2 = fibonacci(n)
print(result1, result2)