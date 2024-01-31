s = input()
str = set()

for i in range(1, len(s)+1):
    for j in range(len(s)):
        str.add(s[j:j+i])
print(len(str))