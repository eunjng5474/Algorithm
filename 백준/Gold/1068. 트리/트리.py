import sys
input = sys.stdin.readline

def dfs(x):
    lst[x] = -2
    for i in child[x]:  # 자식 중 제거되지 않은 노드에 대해 재귀
        if lst[i] != -2:
            dfs(i)

n = int(input())
lst = list(map(int, input().split()))
child = [[] for _ in range(n)]
for i in range(n):
    if lst[i] == -1:
        continue
    child[lst[i]].append(i)

remove = int(input())
dfs(remove)
cnt = 0

for i in range(n):
    flag = True
    if lst[i] == -2:
        flag = False
        continue

    for j in child[i]:      # 자식 중 하나라도 -2가 아닌 게 있다면
        if lst[j] != -2:    # 자식이 있는 것이므로 flag를 False로
            flag = False
            break
    if flag:                # flag가 True이면 자식이 없음
        cnt += 1

print(cnt)