MAX_NUM = 45


def get_args():
    num_of_testcases = int(input())
    test_cases = []
    for _ in range(num_of_testcases):
        test_cases.append(int(input()))
    return num_of_testcases, test_cases


def solution(test_case):
    answer = [(0, 0)] * MAX_NUM
    answer[0], answer[1] = (0, 1), (1, 0)
    for i in range(2, test_case + 1):
        num_zero = answer[i-1][0] + answer[i-2][0]
        num_one = answer[i-1][1] + answer[i-2][1]
        answer[i] = (num_zero, num_one)
    return answer[test_case]


def main():
    num_of_testcases, test_cases = get_args()
    answer = []
    for test_case in test_cases:
        answer.append(solution(test_case))

    for i in range(num_of_testcases):
        print(answer[i][0], answer[i][1])


if __name__ == '__main__':
    main()
