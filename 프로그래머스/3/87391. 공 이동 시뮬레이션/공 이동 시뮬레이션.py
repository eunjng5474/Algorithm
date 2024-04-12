def solution(n, m, x, y, queries):
    # x최소, x최대, y최소, y최대
    x1, x2, y1, y2 = x, x, y, y
    
    for d, dx in reversed(queries):
        if d == 0:      # <- 방향이므로 반대 방향인 ->로 계산
            y2 = min(y2 + dx, m-1)
            # -> 방향으로 dx만큼 더 갈 수 있으므로 y의 최대값 += dx || 범위 벗어날 경우 m-1
            # y1이 0이 아니라면 최소값인 y1에도 dx를 더한다.
            if y1 != 0:
                y1 += dx
                
        elif d == 1:      # ->
            y1 = max(y1 - dx, 0)
            # 반대인 <- 방향으로 dx만큼 갈 수 있으므로 y2 -= dx || 0
            if y2 != m-1:
                y2 -= dx
        
        elif d == 2:
            x2 = min(x2 + dx, n-1)
            if x1 != 0:
                x1 += dx
        
        elif d == 3:
            x1 = max(x1 - dx, 0)
            if x2 != n-1:
                x2 -= dx
        
        # 범위를 아예 벗어날 경우 0
        if y1 >= m or y2 < 0 or x1 >= n or x2 < 0:
            return 0
    
    return (x2 - x1 + 1) * (y2 - y1 + 1)