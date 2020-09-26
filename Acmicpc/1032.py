def get_args():
    num_of_file = int(input())
    file_name = []
    for i in range(num_of_file):
        file_name.append(input())
    return num_of_file, file_name


def solution(num_of_file, file_name):
    file_length = len(file_name[0])
    if num_of_file == 1:
        return file_name[0]
    ans = ""
    for j in range(file_length):
        for i in range(num_of_file-1):
            if file_name[i][j] != file_name[i + 1][j]:
                ans += '?'
                break
            if i == num_of_file-2:
                ans += file_name[0][j]
    return ans


if __name__ == '__main__':
    n, file_list = get_args()
    result = solution(n, file_list)
    print(result)
