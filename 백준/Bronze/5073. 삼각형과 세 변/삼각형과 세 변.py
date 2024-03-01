import sys
input = sys.stdin.readline

while(True):
    lst = sorted(list(map(int, input().split())))
    a = lst[0]
    b = lst[1]
    c = lst[2]
    if a == b == c == 0:
        break
    if c >= a + b:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")