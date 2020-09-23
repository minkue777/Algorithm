def solution(money, M):
    d = [0] * (max(money+[M]) + 1)
    for m in money:
        d[m] = 1
    for i in range(1, M+1):
        l = []
        for m in money:
            if i > m  and d[i] == 0 and d[i-m] != 0:
                l.append(d[i-m] + 1)
        if l:
            d[i] = min(l)
        print(d)
    return d[M]

#a = [k for k in range(1, 101)]
a = [1, 2, 3]
print(solution(a, 3))
                
        