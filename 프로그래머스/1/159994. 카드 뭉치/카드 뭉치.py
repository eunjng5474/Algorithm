def solution(cards1, cards2, goal):
    n = len(cards1)
    m = len(cards2)
    i, j = 0, 0
    
    for g in goal:
        if i < n and cards1[i] == g:
            i += 1
        if j < m and cards2[j] == g:
            j += 1
    
    if i+j == len(goal):
        return "Yes"
    
    return "No"