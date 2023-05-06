import sys
input = sys.stdin.readline

rotate = [i for i in range(1, 21)]
rotate += [32, 22, 23, 24, 30, 26, 24, 28, 29, 24, 31, 20, 32]

game = []  # 게임판 점수
for s in range(0, 41, 2):
    game.append(s)
game += [13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]

dice = list(map(int, input().split()))
horse = [0, 0, 0, 0]
turn = {5: 21, 10: 25, 15: 27}
result = 0

def sol(idx, score):
    global result
    if idx >= 10:
        result = max(result, score)
        return

    for i in range(4):
        h = horse[i]
        if h in turn:
            h = turn[h]
        else:
            h = rotate[h]

        for j in range(1, dice[idx]):
            h = rotate[h]
        if h == 32 or (h < 32 and h not in horse):
            tmp = horse[i]
            horse[i] = h
            sol(idx + 1, score + game[h])
            horse[i] = tmp

sol(0, 0)
print(result)