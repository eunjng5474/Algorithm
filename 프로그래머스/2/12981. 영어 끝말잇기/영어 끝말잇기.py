def solution(n, words):
    answer = []
    check = [words[0]]
    
    for i in range(1, len(words)):
        if words[i][0] != check[-1][-1] or words[i] in check:
            answer = [i%n + 1, i//n + 1]
            break
        check.append(words[i])
    
    if not answer:
        answer = [0, 0]
    return answer