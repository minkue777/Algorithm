import heapq

def get_args():
    food_times = list(map(int, input('음식 시간 : ').split()))
    k = int(input('중지 시간 : '))
    return food_times, k

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    
    sum_times = 0
    previous = 0
    length = len(food_times)
    while sum_times + length * (q[0][0]-previous) <= k:
        now = heapq.heappop(q)[0]
        sum_times += length * (now - previous)
        length -= 1
        previous = now
    
    result = sorted(q, key = lambda x: x[1])
    return result[(k - sum_times) % length][1]

food_times, k = get_args()
print(solution(food_times, k))