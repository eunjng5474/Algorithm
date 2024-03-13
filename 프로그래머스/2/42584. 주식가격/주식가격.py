def solution(prices):
    # 떨어진 적 없을 때의 초 기록(prices 길이만큼의 역순)
    answer = [i for i in range(len(prices)-1, -1, -1)]
    stack = []
    
    for i, p in enumerate(prices):
        while stack and stack[-1][1] > p:
            # stack의 마지막 값의 가격이 현재 가격(p)보다 크면
            # pop하고 answer에서 해당 인덱스의 값을 i - idx로
            # (idx부터 i까지만 가격이 떨어지지 않은 것)
            idx, prc = stack.pop()
            answer[idx] = i - idx
        stack.append((i, p))

    return answer