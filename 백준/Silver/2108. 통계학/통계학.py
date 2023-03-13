import sys
input = sys.stdin.readline

N = int(input())
nums = sorted([int(input()) for _ in range(N)])

mid_idx = N//2
print(round(sum(nums)/N))
print(nums[mid_idx])

mode_dic = {}

for i in nums:
    if i in mode_dic:
        mode_dic[i] += 1
    else:
        mode_dic[i] = 1

mode_lst = [k for k, v in mode_dic.items() if max(mode_dic.values()) == v]
# print(mode_lst)
if len(mode_lst) == 1:
    print(mode_lst[0])
else:
    print(mode_lst[1])


if nums[-1] * nums[0] < 0:
    print(nums[-1] + abs(nums[0]))
else:
    print(nums[-1] - nums[0])