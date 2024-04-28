answer = 100000001

def solution(storey):
    
    def dfs(now, cnt):
        global answer
        if now == 0:
            answer = min(cnt, answer)
            return
        if cnt > answer:
            return
        
        n = now % 10
        if n < 5:       # 1의 자리가 5 미만이면 내려가기 
            dfs(now // 10, cnt + n)
        elif n > 5:     # 5보다 크면 +10으로 올라간 뒤 내려가기 
            dfs(now // 10 + 1, cnt + (10-n))
        else:           # 5일 때는 두 개 다 해보기 
            dfs(now // 10, cnt + n)
            dfs(now // 10 + 1, cnt + (10-n))
    
    dfs(storey, 0)
    return answer