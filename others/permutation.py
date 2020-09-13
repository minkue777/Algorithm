from itertools import permutations
import copy
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

def findIdx(arr):
    N = len(arr)
    for i in range(N-2, -1, -1):
        if arr[i] < arr[i+1]:
            return i
    return N-1
    
def findMin(arr, idx):
    N = len(arr)
    minimum = arr[idx+1]
    for i in range(idx+1, N):
        if arr[i] > arr[idx] and arr[i] < minimum:
            minimum = arr[i]
        
    return arr.index(minimum)

def changeNum(arr, idx1, idx2):
    temp = arr[idx2]
    arr[idx2] = arr[idx1]
    arr[idx1] = temp
    
def reOrder(arr, idx):
    start = idx + 1
    end = len(arr) - 1
    while (start <= end):
        changeNum(arr, start, end)
        start += 1
        end -= 1
        
def nextPermutation(arr):
    new_arr = copy.deepcopy(arr)
    idx1 = findIdx(new_arr)
    idx2 = findMin(new_arr, idx1)
    changeNum(new_arr, idx1, idx2)
    reOrder(new_arr, idx1)
    return new_arr

@proc_time
def solution(n, k):
    arr = [i for i in range(1, n+1)]
    while k-1:
        arr = nextPermutation(arr)
        k -= 1
    return arr


print(solution(7, 323))
    