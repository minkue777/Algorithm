def getArgs():
    n, m = map(int, input().split())
    lamp = []
    for i in range(n):
        l = []
        row = input()
        for k in row:
            l.append(int(k))
        lamp.append(l)
    k = int(input())
    return n, m, lamp, k


def numZeros(row):
    count = 0
    for c in row:
        count += (c == 0)
    return count


n, m, lamp, k = getArgs()
Klamp = [r for r in lamp if (numZeros(r) <= k and (k-numZeros(r))%2 == 0)]
d = [False] * len(Klamp)
ans = 0

for i in range(len(Klamp)):
    if d[i]:
        continue
    count = 1
    d[i] = True
    for j in range(i+1, len(Klamp)):
        if Klamp[i] == Klamp[j]:
            d[j] = True
            count += 1
    ans = max(ans, count)
    
print(ans)


            
        







        

