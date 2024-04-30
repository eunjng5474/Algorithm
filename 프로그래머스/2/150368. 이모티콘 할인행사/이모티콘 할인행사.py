from itertools import product

def solution(users, emoticons):
    n = len(emoticons)
    sales = list(product([10, 20, 30, 40], repeat = n))
    cnt, price = 0, 0
    
    for sale in sales:
        c, p = 0, 0
        for user in users:
            tmp = 0
            for i in range(n):
                if sale[i] >= user[0]:
                    tmp += (emoticons[i] * (100 - sale[i]) // 100)
            if tmp >= user[1]:
                c += 1
            else:
                p += tmp
                
        if c > cnt:
            cnt = c
            price = p
        elif c == cnt:
            price = max(price, p)
            
    return [cnt, price]