from collections import deque

def solution(bridge_length, limit, truck_weight):
    total_time = 0
    zeros = [0] * bridge_length
    bridge = deque(zeros, maxlen=bridge_length)
    truck_weight.reverse()
    total_weight = 0
    
    while True:
        if len(truck_weight) == 0 or truck_weight[-1] + total_weight - bridge[-1] > limit:
            total_weight -= bridge[-1]
            bridge.appendleft(0)
        else:
            total_weight -= bridge[-1]
            bridge.appendleft(truck_weight.pop())
            total_weight += bridge[0]
            
        total_time += 1
        print(bridge, total_time)
        
        if len(truck_weight) == 0 and total_weight == 0:
            return total_time
            

        
    
    
    

    