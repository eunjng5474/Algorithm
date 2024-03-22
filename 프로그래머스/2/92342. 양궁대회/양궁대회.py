from copy import deepcopy

answer = []
score = 0

def check(tmp, info):
    apeach, ryan = 0, 0
    for i in range(10):
        if info[i] == tmp[i] == 0:
            continue
        if info[i] >= tmp[i]:
            apeach += 10-i
        else:
            ryan += 10-i
    return ryan - apeach

def dfs(idx, cnt, tmp, info):
    global answer, score
    if idx == 11:
        s = check(tmp, info)
        if cnt:
            tmp[10] = cnt
        if s <= 0:
            return
        lst = deepcopy(tmp)
        if s > score:
            score = s
            answer = [lst]
        elif s == score:
            answer.append(lst)
        return
        
    if cnt > info[idx]:
        m = info[idx] + 1
        tmp[idx] = m
        dfs(idx+1, cnt-m, tmp, info)
    tmp[idx] = 0
    dfs(idx+1, cnt, tmp, info)

    
def solution(n, info):
    global answer
    tmp = [0] * 11
    dfs(0, n, tmp, info)
    
    answer.sort(key=lambda x:x[::-1], reverse=True)
    if not answer:
        answer = [-1]
    else:
        answer = answer[0]
    
    return answer
