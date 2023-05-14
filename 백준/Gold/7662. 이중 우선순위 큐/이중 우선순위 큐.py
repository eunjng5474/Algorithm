import sys
input = sys.stdin.readline
import heapq

T = int(input())
for tc in range(T):
    min_hq = []
    max_hq = []
    k = int(input())
    used = [0] * k

    for i in range(k):
        cal, n = input().split()
        if cal == 'I':
            # 값과 인덱스 i를 튜플 형태로 같이 push
            heapq.heappush(min_hq, (int(n), i))
            heapq.heappush(max_hq, (-int(n), i))
            used[i] = 1

        elif n == '1':
            while max_hq and not used[max_hq[0][1]]:
                # 사용된 정수(used가 1인 경우) 모두 제거
                heapq.heappop(max_hq)
            if max_hq:
                used[max_hq[0][1]] = 0
                # 값 없다는 표시 
                heapq.heappop(max_hq)

        else:
            while min_hq and not used[min_hq[0][1]]:
                heapq.heappop(min_hq)
            if min_hq:
                used[min_hq[0][1]] = 0
                heapq.heappop(min_hq)


    # 사용 안한 정수 나올 때까지가 pop
    while max_hq and not used[max_hq[0][1]]:
        heapq.heappop(max_hq)

    while min_hq and not used[min_hq[0][1]]:
        heapq.heappop(min_hq)

    if max_hq and min_hq:
        print(-max_hq[0][0], min_hq[0][0])
    else:
        print('EMPTY')