def solution(name):
    n = len(name)
    
    answer = 0
    cnt = n - 1 # 왼/오 최소 이동 횟수
    
    for i in range(n):
        answer += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1) 
        
        # 연속된 A 찾기 
        j = i + 1
        while j < n and name[j] == 'A':
            j += 1
        
        cnt = min([cnt, 2 * i + n - j, i + 2 * (n - j)])
    answer += cnt
    return answer