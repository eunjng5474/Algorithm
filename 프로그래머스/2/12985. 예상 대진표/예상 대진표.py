def solution(n,a,b):
    answer = 0

    while True:
        answer += 1
        if abs(a-b) == 1 and min(a, b) % 2:
            break
            
        if a % 2:
            a = a//2 + 1
        else:
            a //= 2
        if b % 2:
            b = b//2 + 1
        else:
            b //= 2

    return answer