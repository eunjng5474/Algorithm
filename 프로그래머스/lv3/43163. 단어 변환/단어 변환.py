def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = 1e9
    used = [False for _ in range(len(words))]
    
    def dfs(word, cnt):
        nonlocal answer
        if word == target:
            answer = min(answer, cnt)
            return
        
        for w in range(len(words)):
            if used[w] == True:
                continue
            
            tmp = 0
            for i in range(len(words[w])):
                if word[i] != words[w][i]:
                    tmp += 1
            if tmp == 1:
                used[w] = True
                dfs(words[w], cnt+1)
                used[w] = False
        
    dfs(begin, 0)        
    return answer