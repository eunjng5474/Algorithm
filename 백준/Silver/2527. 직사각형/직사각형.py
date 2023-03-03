for tc in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    if x2 > p1 or y2 > q1 or p2 < x1 or q2 < y1:
        result = 'd'

    elif x1 == p2  or x2 == p1:
        if y2 == q1 or q2 == y1:
            result = 'c'
        else:
            result = 'b'

    elif q1 == y2 or q2 == y1:
        result = 'b'
    else:
        result = 'a'

    print(result)