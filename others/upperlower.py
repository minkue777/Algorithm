def change(s):
    return ''.join([c.upper() if not idx % 2 else c.lower() for idx, c in enumerate(s)])

def solution(s):
    return ' '.join([change(word) for word in s.split(' ')])
    

print(solution("ASDS SDFDF ERER"))