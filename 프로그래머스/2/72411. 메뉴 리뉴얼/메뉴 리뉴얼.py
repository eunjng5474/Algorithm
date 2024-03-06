def solution(orders, course):
    answer = []
    dic = dict()
    max_len = max(course)

    def sol(tmp, idx, order):
        if idx > len(order):
            return
        if len(tmp) > max_len:
            return
        
        if len(tmp) in course:
            lst = sorted(list(tmp))
            tmp = "".join(lst)
            if tmp in dic:
                dic[tmp] += 1
            else:
                dic[tmp] = 1
        
        for i in range(idx, len(order)):
            sol(tmp+order[i], i+1, order)
    
    for o in orders:
        sol("", 0, o)
    
    for c in course:
        words = []
        max_cnt = 1
        for d in dic:
            if len(d) == c:
                if dic[d] > max_cnt:
                    words = [d]
                    max_cnt = dic[d]
                elif dic[d] > 1 and dic[d] == max_cnt:
                    words.append(d)
        for w in words:
            answer.append(w)
    
    return sorted(answer)

