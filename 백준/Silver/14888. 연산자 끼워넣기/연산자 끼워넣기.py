N = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))
calcul = ['+', '-', '*', '//']
used = [0] * 4

max_sum = -int(1e9)
min_sum = int(1e9)
cal = []

def calculator(lst):
    global max_sum, min_sum
    tmp = lst[0]
    for i in range(1, len(lst)):
        if lst[i] == '+':
            tmp += lst[i+1]
        if lst[i] == '-':
            tmp -= lst[i+1]
        if lst[i] == '*':
            tmp *= lst[i+1]
        if lst[i] == '//':
            if tmp < 0:
                ans = -tmp // lst[i+1]
                tmp = -ans
            else:
                tmp //= lst[i+1]

    if tmp > max_sum:
        max_sum = tmp
    if tmp < min_sum:
        min_sum = tmp
    return


def sol(i):
    global cal
    cal.append(nums[i])

    if i == N-1:
        calculator(cal)
        return

    for o in range(4):
        if operator[o] and used[o] != operator[o]:
            cal.append(calcul[o])
            used[o] += 1
            sol(i+1)
            used[o] -= 1
            cal.pop()
            cal.pop()


sol(0)
print(max_sum)
print(min_sum)