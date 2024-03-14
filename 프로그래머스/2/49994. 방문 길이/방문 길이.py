def solution(dirs):
    road = set()
    x, y = 5, 5
    
    for d in dirs:
        if d == "U" and x - 1 >= 0:
            road.add((x, y, x-1, y))    # x, y, nx, ny 추가 
            road.add((x-1, y, x, y))    # 역방향도 추가해줘야 함
            x -= 1
        elif d == "D" and x + 1 < 11:
            road.add((x, y, x+1, y))
            road.add((x+1, y, x, y))
            x += 1
        elif d == "R" and y + 1 < 11:
            road.add((x, y, x, y+1))
            road.add((x, y+1, x, y))
            y += 1
        elif d == "L" and y - 1 >= 0:
            road.add((x, y, x, y-1))
            road.add((x, y-1, x, y))
            y -=1

    # 역방향까지 두 개씩 저장되어있으니 2 나누기
    return len(road) / 2    