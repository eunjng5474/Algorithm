import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()

PN = 'IO'*N + 'I'
p = len(PN)

result = 0
for i in range(M-p+1):
    if S[i:i+p] == PN:
        result += 1
print(result)
