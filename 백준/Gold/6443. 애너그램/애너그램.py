import sys
input = sys.stdin.readline

def sol(cnt, tmp):
    if cnt == len(word):
        print(tmp)
        return

    for i in used:
        if used[i]:
            used[i] -= 1
            sol(cnt+1, tmp+i)
            used[i] += 1

n = int(input())
for _ in range(n):
    used = dict()
    word = sorted(list(input().rstrip()))
    for w in word:
        if w in used:
            used[w] += 1
        else:
            used[w] = 1
    sol(0, "")