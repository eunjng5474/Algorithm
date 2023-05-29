import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
white = 0
blue = 0

def sol(x, y, n):
    global white, blue
    color = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            # 색이 다른 부분 있으면 다시 재귀를 통해 분할 
            if arr[i][j] != color:
                sol(x, y, n//2)
                sol(x, y+n//2, n//2)
                sol(x+n//2, y, n//2)
                sol(x+n//2, y+n//2, n//2)
                return
    # 다 쪼개진 다음 색에 따른 카운트 증가 
    if not color:
        white += 1
    else:
        blue += 1

sol(0, 0, N)
print(white)
print(blue)