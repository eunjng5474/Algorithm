import sys
input = sys.stdin.readline

n =  int(input())
visited = [0] * n
answer = 0

def check(x, y):
    for i in range(x):
        if y == visited[i] or (abs(i - x) == abs(visited[i] - y)):
            return False
    return True

def nqueen(x, visited):
    global answer
    if x == n:
        answer += 1
        return

    for i in range(n):
        if check(x, i):
            visited[x] = i
            nqueen(x+1, visited)
            visited[x] = 0

nqueen(0, visited)
print(answer)