def delChar(string, idx, length=1):
    output = []
    output.append(string[:idx])
    output.append(string[idx+length:])
    return ''.join(output)

def solution(number, k):
    num_str = number
    save_idx = 1
    while k:
        for i in range(save_idx-1, len(num_str)-1):
            if int(num_str[i]) < int(num_str[i+1]):
                num_str = delChar(num_str, i)
                save_idx = max(1, i)
                k -= 1
                break
            
            if i == len(num_str)-2:
                num_str = delChar(num_str, len(num_str)-k, k)
                return num_str

    return num_str

                
    