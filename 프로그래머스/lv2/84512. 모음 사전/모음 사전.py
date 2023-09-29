from itertools import product

def solution(word):    
    words = []
    for i in range(1, 6):
        for j in product(['A', 'E', 'I', 'O', 'U'], repeat = i):
            words.append(''.join(j))
            
    words.sort()
    answer = words.index(word) + 1
    return answer