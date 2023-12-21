def solution(s):
    answer = True
    
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack and stack.pop() == "(":
                continue
            answer = False
            break
    if stack:
        answer = False
    return answer