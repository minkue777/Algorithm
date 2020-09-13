import copy
import numpy as np

def sol(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0

def numPaper(citations, n):
    citations = np.array(citations)
    return sum(citations >= n)

def solution(citations):
    
    new_citations = copy.deepcopy(citations)
    new_citations.sort()
    N = len(new_citations)
    H_index = []
    
    for idx in range(N+1):
        if numPaper(new_citations, idx) >= idx:
            H_index.append(idx)
    
    return H_index[-1]
    
print(sol([0, 0, 2]))