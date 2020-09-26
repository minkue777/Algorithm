def get_args():
    num_of_file = int(input())
    file_name = []
    for i in range(num_of_file):
        file_name.append(input())
    return num_of_file, file_name


def solution():
    n, file_list = get_args()
    file_length = len(file_list[0])
    ans = ""
    for j in range(file_length):
        for i in range(n-1):
            if file_list[i][j] != file_list[i+1][j]:
                ans += '?'
                break
            if i == n-2:
                ans += file_list[0][j]
    return ans


result = solution()
print(result)






