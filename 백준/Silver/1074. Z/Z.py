import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
cnt = 0
answer = 0

def sol(x, y, n):
    global cnt, answer
    if x == r and y == c:
        answer = cnt
        return

    if not ((x <= r < x+n) and (y <= c < y+n)):
        cnt += n**2
        return
    if n == 1:
        cnt += 1
        return

    sol(x, y, n//2)
    sol(x, y+n//2, n//2)
    sol(x+n//2, y, n//2)
    sol(x+n//2, y+n//2, n//2)

sol(0, 0, 2**N)
print(answer)