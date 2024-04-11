def solution(k, ranges):
    answer = []
    # 콜라츠 추측
    collatz = [k]
    while k != 1:
        if not k % 2:
            k //= 2
        else:
            k = k * 3 + 1
        collatz.append(k)
    n = len(collatz) - 1
    
    # 이전 인덱스에서 해당 인덱스까지의 넓이 저장(항상 x의 길이 1) 
    area = [0]
    for i in range(1, len(collatz)):
        area.append((collatz[i-1] + collatz[i]) / 2)

    for a, b in ranges:
        if a > n + b:
            answer.append(-1)
            continue
        answer.append(sum(area[a+1:n+b+1]))
        
    return answer