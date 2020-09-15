def checkPriority(priority):
    pivot = priority[0]
    result = True
    for p in priority[1:]:
        if pivot < p:
            result = False
            break
    return result

def printDocument(document, priority):
    x = document[0]
    del document[0]
    del priority[0]
    return x

def reorder(document, priority):
    document.append(document[0])
    del document[0]
    priority.append(priority[0])
    del priority[0]

def my_solution(priority, location):
    N = len(priority)
    document = [x for x in range(N)]
    count = 0
    while True:
        print(document, priority, count)
        if checkPriority(priority):
            count += 1
            x = printDocument(document, priority)
            if x == location:
                return count
        else:
            reorder(document, priority)

            
            
def other_solution(priorities, location):
    queue =  [(idx ,p) for idx, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer