x = int(input())
line = 1

while x > line:
    x -= line
    line += 1

if line % 2:
    a = line - x + 1
    b = x
else:
    a = x
    b = line - x + 1

print(a, "/", b, sep="")