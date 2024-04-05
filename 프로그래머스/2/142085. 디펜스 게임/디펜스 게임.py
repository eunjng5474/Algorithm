from heapq import heappop, heappush

def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    
    answer = 0
    num = 0
    hq = []
    
    for e in enemy:
        # heappop은 가장 작은 값을 제거하는데
        # e가 가장 클 때 무적권을 사용해야 하므로 음수로 저장 
        heappush(hq, -e)
        num += e
        if num > n:
            # 적의 수의 합이 n보다 큰데 무적권도 없으면 불가 -> break
            if not k:
                break
            # 남아있으면 heappop을 통해 해당 적의 수에 대해 무적권 사용
            k -= 1
            # 해당 수만큼 적이 없는 것이나 마찬가지이므로 num에서 다시 빼는데
            # 음수로 저장했으니까 더해줘야 함
            num += heappop(hq)
        answer += 1
    
    return answer