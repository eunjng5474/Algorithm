def solution(tickets):
    tickets.sort(key=lambda x: (x[1], x[0]))
    answer = []
    tmp = ["ICN"]
    visited = [0] * len(tickets)

    def dfs(start, tmp):
        if 0 not in visited:
            answer.append(tmp)
            return

        for i in range(len(tickets)):
            if tickets[i][0] == start and not visited[i]:
                visited[i] = 1
                dfs(tickets[i][1], tmp+[tickets[i][1]])
                visited[i] = 0

    dfs("ICN", tmp)
    return answer[0]