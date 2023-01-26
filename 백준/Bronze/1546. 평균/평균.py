n = int(input())
scores = list(map(int, input().split()))
m = max(scores)
new_sc = []
for i in scores:
    new_sc.append((i/m*100))
print(sum(new_sc) / len(new_sc))