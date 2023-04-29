def solution(user_id, banned_id):
    answer = 0
    result = []
    used = [0] * len(user_id)

    def check(b_idx, tmp, cnt):
        if cnt == len(banned_id):
            ans = list(tmp)
            result.append(ans)
            return

        for u in range(len(user_id)):
            flag = True
            if len(banned_id[b_idx]) != len(user_id[u]):
                flag = False
                continue
            for b in range(len(banned_id[b_idx])):
                if banned_id[b_idx][b] == '*':
                    continue
                if banned_id[b_idx][b] != user_id[u][b]:
                    flag = False
                    break
            if flag:
                if not used[u]:
                    used[u] = 1
                    tmp[b_idx] = user_id[u]
                    check(b_idx + 1, tmp, cnt+1)
                    used[u] = 0
                    tmp[b_idx] = ""

    tmp = ["" for _ in range(len(banned_id))]
    check(0, tmp, 0)

    answer_lst = []
    for r in range(len(result)):
        result[r].sort()
        if result[r] not in answer_lst:
            answer_lst.append(result[r])

    answer = len(answer_lst)
    return answer