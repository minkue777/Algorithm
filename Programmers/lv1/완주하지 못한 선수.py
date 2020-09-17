import collections

def solution1(participant, completion):
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

def solution2(participant, completion):
    d = {}
    for person in participant:
        d[person] = d.get(person, 0) + 1
    for person in completion:
        d[person] -= 1
    
    ans = [k for k, v in d.items() if v == 1]
    return ans[0]
    
solution2(["Lee", 'Lee', 'jin'], ['Lee'])