from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
                
            
    def bfs(x, y, dest):
        q = deque()
        q.append((x, y))
        visited = [[-1] * m for _ in range(n)]     
        visited[x][y] = 0

        while q:
            flag = False
            x, y = q.popleft()
            
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if maps[nx][ny] == "X" or visited[nx][ny] > -1:
                    continue
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

                if maps[nx][ny] == dest:
                    return visited[nx][ny]
        return -1

    
    lx, ly = 0, 0
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                cnt1 = bfs(i, j, "L")
            elif maps[i][j] == "L":
                lx, ly = i, j
    
    cnt2 = bfs(lx, ly, "E")
    if cnt1 == -1 or cnt2 == -1:
        answer = -1
    else:
        answer = cnt1 + cnt2
    
    return answer




