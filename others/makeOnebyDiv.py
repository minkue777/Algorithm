def solution(n):
    DP_Table = [0] * (n+1)
    DP_Table[1] = 0
    DP_Table[2] = 1
    
    for i in range(3, n+1):
        l = []
        if i % 5 == 0:
            l.append(DP_Table[i//5]+1)
        if i % 3 == 0:
            l.append(DP_Table[i//3]+1)
        if i % 2 == 0:
            l.append(DP_Table[i//2]+1)
        l.append(DP_Table[i-1]+1)
        print(l)
        DP_Table[i] = min(l)
    
    print(DP_Table)
    return DP_Table[n]

solution(26)