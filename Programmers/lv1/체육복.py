def remove(i, lost, reserve):
    if i in reserve:
        reserve.remove(i)
        return True
    elif i-1 in reserve:
        reserve.remove(i-1)
        return True
    elif i+1 in reserve and i+1 not in lost:
        reserve.remove(i+1)
        return True
    else:
        return False
    
def solution(n, lost, reserve):
    max_student = n - len(lost)
    for i in lost:
        if remove(i, lost, reserve):
            max_student += 1
    return max_student
