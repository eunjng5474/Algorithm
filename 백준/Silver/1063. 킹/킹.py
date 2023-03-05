# arr = [[0] * 9 for _ in range(9)]
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

dx = [1, -1, 0, 0, 1, 1, -1, -1] #상하좌우 좌상 우상 좌하 우하
dy = [0, 0, -1, 1, -1, 1, -1, 1]

move = {'R': 3, 'L': 2, 'B': 1, 'T': 0, 'RT': 5, 'LT': 4, 'RB': 7, 'LB': 6}


k, s, N = input().split()
king_x = int(k[1])
king_y = alphabet.index(k[0]) + 1
stone_x = int(s[1])
stone_y = alphabet.index(s[0]) + 1
# arr[king_x][king_y] = 'K'
# arr[stone_x][stone_y] = 'S'


lst = list(input() for _ in range(int(N)))

kx, ky = king_x, king_y
sx, sy = stone_x, stone_y
for l in lst:

    nkx, nky = kx + dx[move[l]], ky + dy[move[l]]
    if 0 < nkx < 9 and 0 < nky < 9:
        if nkx == sx and nky == sy:
            nsx, nsy = sx + dx[move[l]], sy + dy[move[l]]
            if 0 < nsx < 9 and 0 < nsy < 9:
                # arr[sx][sy], arr[nsx][nsy] = arr[nsx][nsy], arr[sx][sy]
                sx, sy = nsx, nsy
            else:
                continue
        # arr[kx][ky], arr[nkx][nky] = arr[nkx][nky], arr[kx][ky]
        kx, ky = nkx, nky

king_result = ''
stone_result = ''

king_result += alphabet[ky-1]
king_result += str(kx)
stone_result += alphabet[sy-1]
stone_result += str(sx)

print(king_result)
print(stone_result)
