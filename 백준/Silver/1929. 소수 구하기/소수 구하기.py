import sys
input = sys.stdin.readline

M, N = map(int, input().split())
prime = [True] * (N+1)
prime[0] = False
prime[1] = False

for i in range(N+1):
    if prime[i]:
        for j in range(i*2, N+1, i):
            prime[j] = False

for i in range(M, N+1):
    if prime[i] == True:
        print(i)