from math import sqrt

def solution(n):
    num = set(range(2,n+1))

    for i in range(2, int(sqrt(n)) + 1):
        if i in num:
            num -= set(range(2*i, n+1, i))
    return len(num)


def sol(n):
    num = [x for x in range(0, n+1)]
    d = [False] * (n+1)
    ans = []
    for k in num[2:]:
        if not d[k]:
            d[k] = True
            ans.append(num[k])
            for i in range(1, n//num[k]+1):
                d[k*i] = True
    print(ans)

            
    
    