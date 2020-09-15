from collections import Counter

def FailureRatio(N, stages):
    count = Counter(stages)
    answer = []
    for i in range(1, N+1):
        try:
            a = count[i]
            b = sum([v for k, v in count.items() if k >= i])
            answer.append(a/b)
        except:
            answer.append(0)
    return answer
        
def ReturnIdx(F):
    result = sorted(range(1, len(F)+1), key=lambda k: F[k-1], reverse=True)
    return result

def solution(N, stages):
    F = FailureRatio(N, stages)
    result = ReturnIdx(F)
    return result

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))