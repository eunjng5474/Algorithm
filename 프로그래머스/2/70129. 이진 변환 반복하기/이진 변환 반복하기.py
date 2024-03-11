def solution(s):
    cnt = 0
    zero = 0
    
    while s != '1':
        tmp = s.count('0')
        zero += tmp
        s = bin(len(s) - tmp)[2:]
        cnt += 1
    
    answer = [cnt, zero]
    return answer