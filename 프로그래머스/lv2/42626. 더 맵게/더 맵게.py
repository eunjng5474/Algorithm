import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while True:
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
        num1 = heapq.heappop(scoville)
        if num1 >= K:
            return answer
        num2 = heapq.heappop(scoville)
        heapq.heappush(scoville, (num1 + num2*2))
        answer += 1
