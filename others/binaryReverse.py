def binaryReverse(string, start, end):
    prev = string[:start]
    present = string[start:end+1]
    future = string[end+1:]
    reverse = ""
    for c in present:
        reverse += '0' if c == '1' else '1'
    return prev + reverse + future


string = input()
count_1 = 0
string_1 = string
while True:
    left_one = string_1.find('1')
    right_one = string_1.rfind('1')
    if left_one == -1:
        break
    string_1 = binaryReverse(string_1, left_one, right_one)
    count_1 += 1

count_0 = 0
string_2 = string
while True:
    left_zero = string_2.find('0')
    right_zero = string_2.rfind('0')
    if left_zero == -1:
        break
    string_2 = binaryReverse(string_2, left_zero, right_zero)
    count_0 += 1

print(count_0, count_1)