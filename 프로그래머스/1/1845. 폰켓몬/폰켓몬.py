def solution(nums):
    n = len(nums)
    nums = set(nums)
    return min(len(nums), n/2)