import heapq

def solution(scoville, K):
    count = 0 
    heapq.heapify(scoville)
    while True:
        m1 = heapq.heappop(scoville)
        if m1 >= K:
            return count
        m2 = heapq.heappop(scoville)
        m1 = m1 + 2*m2
        heapq.heappush(scoville, m1)
        count += 1
        print(scoville, K)
    
solution([1,2,3], 11)