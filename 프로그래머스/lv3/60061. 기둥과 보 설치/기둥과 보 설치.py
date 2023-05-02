
def solution(n, build_frame):
    answer = []

    def check(answer):
        for x, y, num in answer:
            if num:   # 보
                if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                    continue
                return False
                    # if [x, y, 1] in answer or [x, y-1, 0] in answer or [x+1, y-1, 0] in answer:
                    #     return True
            else:   # 기둥
                if y == 0 or [x, y, 1] in answer or [x-1, y, 1] in answer or [x, y-1, 0] in answer:
                    continue
                return False
        return True


    for x, y, a, b in build_frame:
        if b:
            answer.append([x, y, a])
            if not check(answer):
                answer.remove([x, y, a])
        else:
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])

    answer.sort()
    return answer