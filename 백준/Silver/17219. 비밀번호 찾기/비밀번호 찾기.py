import sys
input = sys.stdin.readline

N, M = map(int, input().split())
site = {}
for n in range(N):
    a, b = input().split()
    site[a] = b

for m in range(M):
    s = input().rstrip()
    print(site[s])