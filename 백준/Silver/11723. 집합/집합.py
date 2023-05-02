import sys

M = int(input())
s = set()
for m in range(M):
    inp = sys.stdin.readline().rstrip().split()
    if len(inp) == 1:
        if inp[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
        continue

    if inp[0] == 'add':
        s.add(int(inp[1]))
    elif inp[0] == 'remove':
        s.discard(int(inp[1]))

    elif inp[0] == 'check':
        if int(inp[1]) in s:
            print(1)
        else:
            print(0)

    elif inp[0] == 'toggle':
        if int(inp[1]) in s:
            s.discard(int(inp[1]))
        else:
            s.add(int(inp[1]))