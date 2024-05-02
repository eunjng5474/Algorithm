def solution(genres, plays):
    answer = []
    dic = dict()
    cnt_dic = dict()
    for i, genre in enumerate(genres):
        if genre in dic:
            dic[genre].append((plays[i], i))
            cnt_dic[genre] += plays[i]
        else:
            dic[genre] = [(plays[i], i)]
            cnt_dic[genre] = plays[i]
    
    for d in dic:
        dic[d].sort(key = lambda x : x[0], reverse=True)
    cnt_dic = sorted(cnt_dic.items(), key = lambda x : x[1], reverse=True)
    
    for genre, cnt in cnt_dic:
        for i in range(min(2, len(dic[genre]))):
            answer.append(dic[genre][i][1])
    
    return answer