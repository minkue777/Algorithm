from collections import deque

def change124(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3) 
        return change124(q) + '124'[r]

def quotient(n):
    q = n % 3
    if q == 0:
        return 3
    elif q == 1:
        return 1
    elif q == 2:
        return 2

def solution(n):
    numString = ''
    d = deque()

    while True:
        q = quotient(n)
        if q == 1:
            d.append('1')
        elif q == 2:
            d.append('2')
        elif q == 3:
            d.append('4')
            
        if n <= 3:
            break
        n = int((n - q)/3)
        
    while d:
        numString += d.pop()    

    return numString

print(change124(6))