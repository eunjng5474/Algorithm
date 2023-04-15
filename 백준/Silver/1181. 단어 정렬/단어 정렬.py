
N = int(input())
lst = [[] for _ in range(51)]
for n in range(N):
    word = input()
    if word not in lst[len(word)]:
        lst[len(word)].append(word)

for l in lst:
    l.sort()
    for i in l:
        print(i)