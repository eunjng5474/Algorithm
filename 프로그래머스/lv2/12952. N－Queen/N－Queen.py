answer = 0

def check(x, y, queen):
    for i in range(x):
        if y == queen[i] or abs(y - queen[i]) == (x-i):
            return False
    return True
    
    # for i in range(n):    # n까지 줄 i에 대해 모두 확인
    #     # n행의 퀸이 있는 열과 i행의 퀸이 있는 열이 같거나
    #     # 행의 차이만큼 퀸이 있는 열의 차이가 같다면 대각선에 위치하는 것이므로 False
    #     if board[n] == board[i] or abs(board[n] - board[i]) == (n-i):
    #         return False
    # return True

def nqueen(x, n, queen):
    global answer
    if x == n:
        answer += 1
        return
    
    for y in range(n):
        if check(x, y, queen):
            queen[x] = y
            nqueen(x+1, n, queen)
    
#     if n == N:          # 행이 N이 되면 N개의 퀸 모두 놓음
#         answer += 1
#         return

#     for i in range(N):
#         if not visited[i]:
#             board[n] = i    # n행의 i열에 퀸을 놓았다는 표시

#             if check(n):
#                 visited[i] = 1  # 방문 표시 후 다음 행 조사
#                 nqueen(n+1)
#                 visited[i] = 0  # 다시 0으로 설정

def solution(n):
    global answer
    queen = [0] * n
    # visited = [0] * n
    
    nqueen(0, n , queen)

    return answer