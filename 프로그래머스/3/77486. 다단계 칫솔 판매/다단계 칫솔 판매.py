def solution(enroll, referral, seller, amount):
    n = len(enroll)
    answer = [0 for _ in range(n)]
    index = {}
    for i in range(n):
        index[enroll[i]] = i
    
    def dfs(name, money):
        cal = money // 10
        i = index[name]
        answer[i] += (money - cal)
        if cal < 1:
            return
        if referral[i] == "-":
            return
        dfs(referral[i], cal)
        

    for i in range(len(seller)):
        dfs(seller[i], amount[i] * 100)
    
    return answer