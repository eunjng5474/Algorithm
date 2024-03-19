def solution(s):
    answer = 0
    
    def check(string):
        stack = []
        for st in string:
            if st in ["(", "[", "{"]:
                stack.append(st)
            else:
                if not stack:
                    return False
                p = stack.pop()
                if st == ")":
                    if p != "(":
                        return False
                elif st == "]":
                    if p != "[":
                        return False
                elif st == "}":
                    if p != "{":
                        return False
        if not stack:
            return True
    
    for i in range(len(s)):
        if s[0] not in [")", "]", "}"]:
            if check(s):
                answer += 1
        s = s[1:] + s[0]
        
    
    return answer