dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(land):
    n = len(land)
    m = len(land[0])
    
    lst = [0] * m
    visited = [[False] * m for _ in range(n)]
    
    def dfs(i, j):
        stack = []
        stack.append((i, j))
        visited[i][j] = True
        l, r = j, j     # 해당 구역 내 가장 왼쪽 열과 오른쪽 열
        cnt = 1
        
        while stack:
            x, y = stack.pop()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if visited[nx][ny] or not land[nx][ny]:
                    continue
                visited[nx][ny] = True
                cnt += 1
                l = min(l, ny)
                r = max(r, ny)
                stack.append((nx, ny))
        
        return l, r, cnt
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] or not land[i][j]:
                continue
            l, r, cnt = dfs(i, j)
            for k in range(l, r+1):
                lst[k] += cnt
                
    return max(lst)