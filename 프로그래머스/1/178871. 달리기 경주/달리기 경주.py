def solution(players, callings):
    answer = []
    rank = dict()
    
    for i, p in enumerate(players):
        rank[p] = i
    
    for c in callings:
        idx = rank[c]
        p1, p2 = players[idx-1], players[idx]
        players[idx-1], players[idx] = p2, p1
        rank[p1] += 1
        rank[p2] -= 1
        
    return players