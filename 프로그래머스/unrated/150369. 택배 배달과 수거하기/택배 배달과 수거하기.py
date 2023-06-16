def solution(cap, n, deliveries, pickups):
    answer = 0
    di = n-1
    pi = n-1
    ds = sum(deliveries)
    ps = sum(pickups)
    
    while ds or ps:
        dist = 0
        
        # 배달
        dcap = cap
        # 먼 곳부터 탐색
        for i in range(di, -1, -1):
            if not deliveries[i]:
                continue
            dist = max(dist, i)
            # 가장 먼 곳까지의 거리 저장
            
            if deliveries[i] <= dcap:
                # 현재 배달 가능 최대 수량보다 적다면
                # 배달(dcap, ds에서 해당 인덱스 값만큼 차감)
                dcap -= deliveries[i]
                ds -= deliveries[i]
                deliveries[i] = 0
            else:
                # 배달 완료 불가
                # 남아있는 dcap만큼만 차감하고, 다음에 i번째 집 가야하니까 di = i 
                deliveries[i] -= dcap
                ds -= dcap
                di = i
                break
                
        # 수거
        pcap = cap
        for i in range(pi, -1, -1):
            if not pickups[i]:
                continue
            dist = max(dist, i)
            
            if pickups[i] <= pcap:
                pcap -= pickups[i]
                ps -= pickups[i]
                pickups[i] = 0
            else:
                pickups[i] -= pcap
                ps -= pcap
                pi = i
                break
        
        if dist >= 0:
            answer += (dist+1)*2 # 왕복
        
    return answer 