def solution(s):
    answer = 0
    for idx, num in enumerate(s[::-1]):
        if num == '-':
            return -answer
        elif num == '+':
            return answer
        
        answer += int(num)*(10**idx)
    return answer

