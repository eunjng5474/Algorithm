def solution(want, number, discount):
    answer = 0
    for i in range(len(discount) - 9):
        check = [0] * len(want)
        cnt = sum(number)

        for j in range(10):
            if discount[i+j] in want:
                check[want.index(discount[i+j])] += 1
                cnt -=1
        if not cnt:
            if check == number:
                answer += 1
    
    return answer