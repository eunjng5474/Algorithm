import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

tp = (p + t) // w
tq = (q + t) // h

if not tp % 2:
    x = (p+t) % w
else:
    x = w - ((p+t) % w)

if not tq % 2:
    y = (q+t) % h
else:
    y = h - ((q+t) % h)

print(x, y)