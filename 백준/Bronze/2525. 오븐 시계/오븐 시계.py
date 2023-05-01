h, m = map(int, input().split())
t = int(input())
t_h = t // 60
t_m = t % 60
if m + t_m >= 60:
    h += 1
    m -= 60
if h + t_h < 24:
    print(f'{h + t_h} {m + t_m}')
else:
    print(f'{(h + t_h)-24} {m + t_m}')