def solution(number, k):
    answer = ''
    stack = []
    
    for n in number:
        while k > 0:
            if not stack or n <= stack[-1]:
                break
            stack.pop()
            k -= 1
        stack.append(n)
    
    stack = stack[:len(number)-k]
    answer = ''.join(stack)
        
    return answer