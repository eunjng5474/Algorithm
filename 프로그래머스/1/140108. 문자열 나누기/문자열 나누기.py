def solution(s):
    answer = 1
    x = s[0]
    x_cnt, y_cnt = 0, 0
    
    # 마지막 인덱스에서는 x_cnt, y_cnt와 상관없이 무조건 분해되므로
    # answer을 1로 시작하고, i 범위는 len(s)-1까지
    for i in range(len(s)-1):
        if s[i] == x:
            x_cnt += 1
        else:
            y_cnt += 1
            
        if x_cnt == y_cnt:
            answer += 1
            x = s[i+1]
            x_cnt, y_cnt = 0, 0
            
    return answer