from math import factorial
import time

def proc_time(main):
    def deco(*args, **kwargs):
        ts = time.time()
        result = main(*args, **kwargs)
        elapsed = time.time() - ts
        print("Running time : {}".format(elapsed))
        return result
    return deco

def findN(k):
    count = 1
    while True:
        if factorial(count) > k:
            break
        count += 1
    return count - 1

def remain(k, N, n):
    answer = [0] * (n-N-1)
    while N:
        d = factorial(N)
        answer.append(k // d)
        k %= d
        N -= 1   
    answer.reverse()
    return answer

def makeNewList(ans, n):
    s = [k for k in range(1, n+1) if k not in ans]
    return s

def update(arr, i):
    result = arr[0]
    count = 0
    while count != i:
        result += 1
        if result in arr:
            count += 1
    return result

@proc_time
def solution(n, k):
    ans = []
    arr = makeNewList(ans, n)
    N = findN(k-1)
    R = remain(k-1, N, n)
    
    while arr:
        try:
            v = R.pop()
            ans.append(update(arr, v))
            arr = makeNewList(ans, n)
        except:
            ans.append(arr.pop())
    return ans

@proc_time
def sol(n, k):
    from math import factorial
    answer = []
    order = list(range(1,n+1))
    while n!=0 :
        fact = factorial(n-1)
        #answer.append(order.pop(k//fact-1 if k%fact ==0 else k//fact))
        answer.append(order.pop((k-1)//fact))
        n,k = n-1, k%fact
    return answer


print(sol(20, 334539485739485739))