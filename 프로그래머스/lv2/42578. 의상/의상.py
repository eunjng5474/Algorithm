def solution(clothes):
    dict = {}
    answer = 1
    for name, type in clothes:
        if type in dict:
            dict[type].append(name)
        else:
            dict[type] = [name]
    
    for d in dict:
        answer *= (len(dict[d]) + 1) 
    answer -= 1
    
    return answer