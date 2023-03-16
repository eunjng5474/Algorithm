from itertools import permutations

def prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if not n % i:
                return False
    return True


def solution(numbers):
    answer = 0
    nums = []
    for i in range(1, len(numbers) + 1):
        nums.append(list(set(map(''.join, permutations(numbers, i)))))
    # permutations(iterable, r) -> 길이가 r인 순열로 반환
    # [['1', '7'], ['71', '17']]
    num = list(set(map(int, set(sum(nums, [])))))
    # [1, 7, 17, 71]

    for n in num:
        if prime(n):
            answer += 1

    return answer