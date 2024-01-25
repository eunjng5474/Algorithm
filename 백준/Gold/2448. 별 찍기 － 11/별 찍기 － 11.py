n = int(input())

def draw(x, y, n):
    if n == 3:
        star[x][y] = '*'
        star[x+1][y-1] = star[x+1][y+1] = '*'
        for i in range(-2, 3):
            star[x+2][y+i] = '*'
    else:
        m = n // 2
        draw(x, y, m)       # 위쪽 삼각형
        draw(x+m, y-m, m)   # 좌측 하단 삼각형
        draw(x+m, y+m, m)   # 우측 하단 삼각형

star = [[' '] * 2 * n for _ in range(n)]
draw(0, n-1, n)
for s in star:
    print(''.join(s))