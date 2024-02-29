import sys
input = sys.stdin.readline

s = input()
result = ""

flag = False
idx = 0

for i in range(len(s)):
    if s[i] == "<":
        if i != 0:
            tmp = s[idx:i]
            result += tmp[::-1]
        flag = True
        idx = i
    elif s[i] == ">":
        result += s[idx:i+1]
        flag = False
        idx = i+1
        continue
    if flag: continue

    if s[i] == " " or i == len(s) - 1:
        tmp = s[idx:i]
        result += tmp[::-1]
        if s[i] == " ":
            result += " "
        idx = i+1

print(result)