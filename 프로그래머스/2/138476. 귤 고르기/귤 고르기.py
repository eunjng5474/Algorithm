def solution(k, tangerine):
    answer = 0
    count = dict()
    for t in tangerine:
        if t in count:
            count[t] += 1
        else:
            count[t] = 1
    count = dict(sorted(count.items(), key = lambda x:x[1], reverse=True))
        
    for i in count.values():
        k -= i
        answer += 1
        if k <= 0:
            break
        
    return answer