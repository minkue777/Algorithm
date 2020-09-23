def val(x, y):
    return True if int(x+y) > int(y+x) else False

def criterion(number):
    ans = 0
    num_str = str(number)
    ans = number * (10**(4 - len(num_str)))
    return ans

def quickSort(numbers):
    arr = list(map(str, numbers))
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    tail = arr[1:]
    
    left_side = [x for x in tail if val(x, pivot)]
    right_side = [x for x in tail if not val(x, pivot)]
    
    return quickSort(left_side) + [pivot] + quickSort(right_side)

def solution(numbers):
    numbers = quickSort(numbers)
    ans = ''.join(numbers)
    if int(ans) == 0:
        return '0'
    return ans
    

