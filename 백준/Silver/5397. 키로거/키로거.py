import sys

T = int(input())
for tc in range(T):
    string = sys.stdin.readline().rstrip()
    left = []
    right = []

    for s in string:
        if s not in '-<>':
            left.append(s)
        else:
            if s == '-' and left:
                left.pop()
            elif s == '<' and left:
                tmp = left.pop()
                right.append(tmp)
            elif s == '>' and right:
                tmp = right.pop()
                left.append(tmp)
    left.extend(reversed(right))
    print(''.join(left))