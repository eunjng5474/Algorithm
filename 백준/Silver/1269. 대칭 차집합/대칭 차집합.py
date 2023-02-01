import sys

a, b = map(int, input().split())

a_set = set(map(int, sys.stdin.readline().split()))
b_set = set(map(int, sys.stdin.readline().split()))

result = len(a_set - b_set) + len(b_set - a_set)
print(result)