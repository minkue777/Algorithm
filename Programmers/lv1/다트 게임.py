import re
def solution(dartResult):
    result = []
    
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i] == '0' and dartResult[i-1] == '1':
                result[-1] *= 10
            else:    
                result.append(int(dartResult[i]))
            
        if dartResult[i] == 'D':
            result[-1] = result[-1] ** 2
        if dartResult[i] == 'T':
            result[-1] = result[-1] ** 3
        if dartResult[i] == '#':
            result[-1] *= -1
        
        if dartResult[i] == '*':
            try:
                result[-2] *= 2
                result[-1] *= 2
            except:
                result[-1] *= 2
    return sum(result)


print(solution("1S2S3S"))
s = "10S2S3S"
p = re.compile('(\d+)([SDT])([*#]?)')
dart = p.findall(s)
