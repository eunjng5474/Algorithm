people1 = [1, 2, 3, 4, 5]
people2 = [2, 1, 2, 3, 2, 4, 2, 5]
people3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]


def solution(answers):
    cnt1, cnt2, cnt3 = 0, 0, 0
    answer = [1]
    cnt_lst = []
    for i in range(len(answers)):
        if answers[i] == people1[i % len(people1)]:
            cnt1 += 1
        cnt_lst.append(cnt1)

        if answers[i] == people2[i % len(people2)]:
            cnt2 += 1

        if answers[i] == people3[i % len(people3)]:
            cnt3 += 1

    if cnt2 == cnt_lst[-1]:
        answer.append(2)
    elif cnt2 > cnt_lst[-1]:
        answer.clear()
        answer.append(2)
        cnt_lst.append(cnt2)


    if cnt3 == cnt_lst[-1]:
        answer.append(3)
    elif cnt3 > cnt_lst[-1]:
        answer.clear()
        answer.append(3)
        cnt_lst.append(cnt3)

    return answer