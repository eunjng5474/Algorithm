def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    
    idx = 0
    for b in B:
        if b > A[idx]:
            answer += 1
            idx += 1
    
    return answer