def change(c, n):
    a = ord(c)
    if a == 32:
        return ' '
    
    if 65 <= a <= 90:
        return chr((a-65 + n) % 26 + 65)

    if 97 <= a <= 122:
        return chr((a-97 + n) % 26 + 97)
def solution(s, n):
    answer = []
    s = list(s)
    for c in s:
        answer.append(change(c, n))
    return ''.join(answer)