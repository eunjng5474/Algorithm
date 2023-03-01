T = int(input())
for i in range(T):
    txt = input()
    result = 0

    cnt = 0
    for i in range(len(txt)):
        if txt[i] == 'O':
            cnt += 1
        else:
            for j in range(cnt+1):
                result += j
                cnt = 0
    for j in range(cnt + 1):
        result += j
    print(result)