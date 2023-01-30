n = int(input())
# if n == 1:
#     print('')

# # n_lst = []

# def func(num):
#     if num == 1:
#         pass
#     for i in range(2, num+1):
#         if num % i == 0 and num//i == 1:
#             return i
#         elif num % i == 0:
#             print(i)
#             return func(num//i)
#             # break
            
#     # elif n == 1:
#     # print('')

# print(func(n))




## sol 2
while n != 0:
    i = 2
    if n == 1:
        break
    # for i in range(2, n+1):
    while i <= n:
        if n % i == 0:
            print(i)
            n = n // i
        else:
            i += 1
    # for i in range(2, n+1):
    #     if n % i == 0:
    #         print(i)
    #         n = n // i
