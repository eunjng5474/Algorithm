def solution(numbers, target):
    answer = 0
    
    def dfs(tmp, idx):
        nonlocal answer
        if idx == len(numbers):
            if tmp == target:
                answer += 1
            return

        dfs(tmp+numbers[idx], idx+1)
        dfs(tmp-numbers[idx], idx+1)
    
    dfs(0, 0)
    return answer
