import sys
input = sys.stdin.readline

n = int(input())
nums = list(int(input()) for _ in range(n))

# # 버블정렬
# for i in range(n):
#     for j in range(n):
#         if nums[i] < nums[j]:
#             nums[i], nums[j] = nums[j], nums[i]
#
# for i in range(n):
#     print(nums[i])

# 삽입정렬
for i in range(1, n):
    while i > 0 and nums[i-1] > nums[i]:
        nums[i-1], nums[i] = nums[i], nums[i-1]
        i -= 1

for i in range(n):
    print(nums[i])