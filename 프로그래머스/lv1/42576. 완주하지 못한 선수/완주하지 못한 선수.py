def solution(participant, completion):
    dict = {}
    answer = ''

    for p in participant:
        if p not in dict:
            dict[p] = 1
        else:
            dict[p] += 1
            
    for c in completion:
        dict[c] -= 1
    
    for d in dict:
        if dict[d]:
            answer = d
            break
    
    return answer