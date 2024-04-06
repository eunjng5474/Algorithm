from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    w = 0   # bridge위의 무게
    
    while bridge:
        answer += 1
        w -= bridge.popleft()
        
        if truck:
            # 무게 초과 안하면 truck[0] 다리 건너기
            if w + truck[0] <= weight:
                t = truck.popleft()
                bridge.append(t)
                w += t
            # 무게 초과시 못 건너니까 0을 추가
            else:
                bridge.append(0)
    return answer