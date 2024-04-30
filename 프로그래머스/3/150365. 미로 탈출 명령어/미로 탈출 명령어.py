import sys
sys.setrecursionlimit(5000)

dx = [1, 0, 0, -1]  # 하좌우상
dy = [0, -1, 1, 0]
dr = "dlru"

def solution(n, m, x, y, r, c, k):
    global answer
    answer = "z"
    dist = abs(r-x) + abs(c-y)
    
    if dist > k or (k - dist) % 2:
        return "impossible"

    def dfs(x, y, cnt, route):
        global answer
        if cnt == k:
            if x == r and y == c:
                answer = route
            return
        if cnt + abs(r-x) + abs(c-y) > k:
            return

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            if nx < 1 or nx > n or ny < 1 or ny > m:
                continue
            if route < answer:
                dfs(nx, ny, cnt+1, route+dr[d])
    
    dfs(x, y, 0, "")
    if answer == "z":
        answer = "impossible"
    return answer