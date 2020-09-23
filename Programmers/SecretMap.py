def num2Sharp(N, num):
    answer = ''
    num_str = bin(num)
    num_str = num_str[2:]
    num_str = 'x'*(N-len(num_str)) + num_str
    
    for i in range(N):
        if num_str[i] == '1':
            answer += '#'
        else:
            answer += 'x'
    return answer

def match(n, s1, s2):
    answer = ''
    for i in range(n):
        if s1[i] == 'x' and s2[i] == 'x':
            answer += ' '
        else:
            answer += '#'
    return answer

def solution(n, arr1, arr2):
    S1 = [num2Sharp(n, num) for num in arr1]
    S2 = [num2Sharp(n, num) for num in arr2]
    S3 = [match(n, s1, s2) for s1, s2 in zip(S1, S2)]
    return S3

def sol(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = str(bin(i|j)[2:])
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

