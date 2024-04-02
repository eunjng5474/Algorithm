def solution(enroll, referral, seller, amount):
    n = len(enroll)
    answer = [0 for _ in range(n)]
    
    # list.index() 사용 시 시간초과 (시간복잡도: O(n))
    # -> index라는 dictionary 만들어서 인덱스 저장 
    index = {}
    for i in range(n):
        index[enroll[i]] = i
    
    def dfs(name, money):
        cal = money // 10
        i = index[name]
        answer[i] += (money - cal)
        
        # 1원 미만이라서 분배할 이득이 없거나
        # 추천인 없으면 return 
        if cal < 1:
            return
        if referral[i] == "-":
            return
        dfs(referral[i], cal)
        

    for i in range(len(seller)):
        dfs(seller[i], amount[i] * 100)
    
    return answer