import sys
input = sys.stdin.readline

string = input().split("-")
result = 0

for i in string[0].split("+"):
    result += int(i)

for j in string[1:]:
    for k in j.split("+"):
        result -= int(k)

print(result)