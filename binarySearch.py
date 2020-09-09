import time
import sys
import random

def proc_time(main):
    def deco(*args, **kwargs):
        ts = time.time()
        main(*args, **kwargs)
        elapsed = time.time() - ts
        print("Running time : {}".format(elapsed))
    return deco

@proc_time
def linearSearch(array, num):
    random.shuffle(array)
    for idx in range(len(array)):
        if array[idx] == num:
            return idx
                
def binarySearch(array, start, end, num):
    mid = (end + start)//2
    if start > end:
        return None
    elif array[mid] == num:
        return mid
    elif array[mid] > num:
        return binarySearch(array, start, mid-1, num)
    else:
        return binarySearch(array, mid+1, end, num)
    
n = int(input("Enter: "))
a = [k for k in range(n)]

ts = time.time()
binarySearch(a, 0, len(a)-1, num=50)
elapsed = time.time() - ts
print("Running time : {}".format(elapsed))
linearSearch(a, 50)