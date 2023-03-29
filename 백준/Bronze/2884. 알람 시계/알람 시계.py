h, m = map(int, input().split())
if m >= 45:
    print(f'{h} {m-45}')
else:
    if h == 0:
        h += 24
    print(f'{h-1} {m+60-45}')