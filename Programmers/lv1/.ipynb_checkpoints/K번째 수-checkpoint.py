def kthNumber(array, command):
    start, end = command[0], command[1]
    cutArray = array[start-1:end]
    cutArray.sort()
    return cutArray[command[2]-1]

def solution(array, commands):
    sol = []
    for c in commands:
        sol.append(kthNumber(array, c))
    return sol


        