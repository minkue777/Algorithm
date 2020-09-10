def solution(n):
    answer = [0] * (n+1)
    for i in range(1, n+1):
        if i == 1:
            answer[1] = 1
            continue
        elif i == 2:
            answer[2] =2
            continue
        else:
            answer[i] = answer[i-1] + answer[i-2]
    return answer[n]
                  
                  
solution(4)