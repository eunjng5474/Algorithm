def solution(sequence, k):
    answer = []
    sum_nums = 0
    l = r = 0
    min_len = 10000002
    
    while l < len(sequence):
        while r < len(sequence):
            if sum_nums >= k:
                break
            sum_nums += sequence[r]
            r += 1
        
        if sum_nums == k:
            if r - l < min_len:
                answer = [l, r - 1]
                min_len = r - l
        
        sum_nums -= sequence[l]
        l += 1

    return answer