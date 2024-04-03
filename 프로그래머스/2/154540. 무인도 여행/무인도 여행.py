from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    answer = []
    visited = [[False] * m for _ in range(n)]
    
    def bfs(x, y, n, m):
        cnt = int(maps[x][y])
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        
        while q:
            x, y = q.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[nx][ny] == "X" or visited[nx][ny]:
                    continue
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += int(maps[nx][ny])
        return cnt

        
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "X" or visited[i][j]:
                continue
            cnt = bfs(i, j, n, m)
            answer.append(cnt)
    if not answer:
        answer = [-1]
    else:
        answer.sort()
        
    return answer