from math import sqrt

def numBrown(yellow_r, yellow_c):
    return (yellow_r+2) * (yellow_c+2) - yellow_r * yellow_c

def solution(brown, yellow):
    for i in range(1, int(sqrt(yellow))+ 1):
        if yellow % i != 0:
            continue
        
        yellow_r, yellow_c = i, yellow // i
        
        if numBrown(yellow_r, yellow_c) == brown:
            return [yellow_c+2, yellow_r+2]
    

print(solution(24, 24))
            
        
    