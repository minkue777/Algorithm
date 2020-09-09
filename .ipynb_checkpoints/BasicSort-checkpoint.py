def selectionSort(arr):
    for i in range(len(arr)-1):
        min_idx = arr.index(min(arr[i:]))
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)

def insertionSort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break
        print(arr)

def simpleQuickSort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quickSort(left_side) + [pivot] + quickSort(right_side)

def quickSort(arr, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quickSort(arr, start, right-1)
    quickSort(arr, right+1, end)    

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
quickSort(arr, 0, len(arr)-1)
print(arr)
