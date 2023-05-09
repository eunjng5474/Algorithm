import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = int(1e9)
height = 0

for i in range(257):
    removed = 0  # 블록 제거 - 1번 작업 
    added = B    # 블록 추가 - 2번 작업 (인벤토리에 있는 블럭 개수 B) 
    for x in range(N):
        for y in range(M):
            if arr[x][y] > i:  # 배열의 높이가 i보다 높으면 블록 추가 
                added += (arr[x][y] - i)
            else:
                removed += (i - arr[x][y])  # 아니면 제거 
    if removed > added:
        continue

    time = (added - B) * 2 + removed  # 추가 블럭에서 처음에 있던 수만큼 빼고 2초 곱한 뒤 제거 각 1초 더하기 
    if time <= result:
        result = time
        height = i

print(result, height)