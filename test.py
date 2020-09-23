def check1(new_id):
    ans = ''
    for c in new_id:
        if 'A' <= c <= 'Z':
            ans += chr(ord(c) - (ord('A') - ord('a')))
        else:
            ans += c
    return ans

def check2(new_id):
    ans = ''
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['_', '-', '.']:
            ans += c
    return ans

def check3(new_id):
    if new_id.find('..') == -1:
        return new_id
    else:
        return check3(new_id.replace("..", "."))

def check4(new_id):
    ans = new_id
    if ans[0] == '.':
        ans = ans[1:]
    if ans == '':
        return ans
    if ans[-1] == '.':
        ans = ans[:-1]
    return ans

def check5(new_id):
    if not new_id:
        return 'a'
    else:
        return new_id
    
def check6(new_id):
    ans = new_id
    if len(new_id) > 15:
        ans = new_id[:15]
    if ans[-1] == '.':
        ans = ans[:-1]
    return ans

def check7(new_id):
    ans = new_id
    while len(ans) < 3:
        ans += new_id[-1]
    return ans
        
def solution(new_id):
    new_id = check1(new_id)
    new_id = check2(new_id)
    new_id = check3(new_id)
    new_id = check4(new_id)
    new_id = check5(new_id)
    new_id = check6(new_id)
    new_id = check7(new_id)
    return new_id

print(solution(check4('=.=')))
    
    