answer = -1

def dfs(k, cnt, dungeons, visited):
    global answer
    if cnt > answer:
        answer = cnt

    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], cnt+1, dungeons, visited)
            visited[i] = False


def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)

    return answer