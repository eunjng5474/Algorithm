from collections import Counter

def solution(topping):
    answer = 0
    a = set()
    b = Counter(topping)
    
    for i in topping:
        b[i] -= 1
        a.add(i)
        if not b[i]:
            b.pop(i)
        if len(a) == len(b):
            answer += 1
        
    return answer