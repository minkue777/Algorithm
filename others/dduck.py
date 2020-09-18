import time

def dduckLength(sortDuck, H):
    ans = 0
    for d in sortDuck:
        if d > H:
            ans += d - H
        else:
            break
    return ans

def solution(dduck, request):
    sortDuck = sorted(dduck, reverse=True)
    dSum = 0
    start = sortDuck[-1]
    end = sortDuck[0]
    ans = 0
    while True:
        ans = (start + end ) // 2
        dSum = dduckLength(sortDuck, ans)
        if dSum > request:
            start = ans+1
        elif dSum < request:
            end = ans-1
            
        print(start, end, ans, dSum)
        if start > end or dSum == request:
            return ans
        

a = sorted([k for k in range(1000000)], reverse=True)
#start = time.time()
ans = solution(a, 2000000000)
print(dduckLength(a, ans))
print(dduckLength(a, ans+1))
#end = time.time()
#print(f'Running Time : {end-start}')
