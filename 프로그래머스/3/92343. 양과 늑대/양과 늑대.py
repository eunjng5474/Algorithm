answer = 0
def solution(info, edges):
    child = [[] for _ in range(len(info))]

    for p, c in edges:
        child[p].append(c)

    def dfs(now, sheep, wolf, able):
        global answer
        
        # 늑대가 양보다 많으면 return, answer을 sheep 최대값으로 갱신 
        if wolf >= sheep:
            return
        if sheep > answer:
            answer = sheep

        # now의 자식 노드들에 대해 갈 수 있으므로 able에 추가 
        able.extend(child[now])

        for a in able:
            # 지금 위치는 가지 않으면서 갈 수 있는 노드들 순회
            # 이때 able 리스트는 새로 만들어야 함
            if info[a]:
                dfs(a, sheep, wolf+1, [i for i in able if i != a])
            else:
                dfs(a, sheep+1, wolf, [i for i in able if i != a])
                
    dfs(0, 1, 0, child[0])
    return answer