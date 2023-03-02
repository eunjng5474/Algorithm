txt = input()
N = len(txt)

for r in range(N, 0, -1):
    if N % r == 0 and r <= (N//r):
        R = r
        C = N//r
        break

for r in range(R):
    for c in range(C):
        print(txt[r+(R*c)], end='')
