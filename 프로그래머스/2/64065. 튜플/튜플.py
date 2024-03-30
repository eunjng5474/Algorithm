def solution(s):
    answer = []
    dic = dict()
    i = 0
    while i < len(s):
        tmp = ""
        while s[i] not in ["{", "}", ","]:
            tmp += s[i]
            i += 1
        if tmp != "":
            if tmp in dic:
                dic[tmp] += 1
            else:
                dic[tmp] = 1
        i += 1
    dic = sorted(dic.items(), key = lambda x:x[1], reverse = True)
    for d in dic:
        answer.append(int(d[0]))
    return answer