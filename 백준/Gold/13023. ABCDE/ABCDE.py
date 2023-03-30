import sys
input = sys.stdin.readline

def sol(n):
    global result
    if len(lst) == 5:
        result = 1
        return

    if n not in lst:
        lst.append(n)

    for i in people[n]:
        if i not in lst:
            lst.append(i)
            sol(i)
            lst.pop()


N, M = map(int, input().split())
people = [[] for _ in range(N)]

for m in range(M):
    a, b = map(int, input().split())
    people[a].append(b)
    people[b].append(a)

result = 0
for i in range(N):
    lst = []
    if not result:
        sol(i)
print(result)