x_nums = []
y_nums = []

for _ in range(3):
    i, j = map(int, input().split())
    x_nums.append(i)
    y_nums.append(j)

for i in range(3):
    if x_nums.count(x_nums[i]) == 1:
        x = x_nums[i]
    if y_nums.count(y_nums[i]) == 1:
        y = y_nums[i]

print(x, y)