import sys
input = sys.stdin.readline

N, M = map(int, input().split())
setA = set(input().rstrip() for _ in range(N))
setB = set(input().rstrip() for _ in range(M))

result = list(setA & setB)
result.sort()
print(len(result))
# print(result)
for i in result:
    print(i)