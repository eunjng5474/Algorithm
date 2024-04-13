def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []  # 인덱스 저장 
    
    for i, n in enumerate(numbers):
        # stack의 마지막 값의 인덱스에 해당하는 수보다 n이 클 동안
        # pop해서 answer에서 해당 인덱스의 값을 n으로 설정
        while stack and n > numbers[stack[-1]]:
            answer[stack.pop()] = n
        stack.append(i)
    
    return answer