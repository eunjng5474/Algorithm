def sol(str):
    global result
    if str == s:
        result = 1
        return
    if len(str) < len(s):
        return

    if str[-1] == "A":
        sol(str[:-1])
    if str[0] == "B":
        sol(str[1:][::-1])

s = input()
t = input()
result = 0
sol(t)
print(result)