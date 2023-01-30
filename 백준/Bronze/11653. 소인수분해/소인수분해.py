n = int(input())

def func(num):
    for i in range(2, num+1):
        if num % i == 0 and num//i == 1:
            print(i)
        elif num % i == 0:
            print(i)
            return func(num//i)

func(n)