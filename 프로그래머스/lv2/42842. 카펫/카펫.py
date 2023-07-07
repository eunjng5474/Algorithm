def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1, total):
        if total%i:
            continue
        j = total//i
        if (i-2)*(j-2) == yellow:
            answer = [j, i]
            break
    
    return answer