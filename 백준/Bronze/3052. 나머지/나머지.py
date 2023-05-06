import sys
input = sys.stdin.readline

lst = []
for n in range(10):
  num = int(input())
  if (num % 42) not in lst:
    lst.append(num % 42)

print(len(lst))