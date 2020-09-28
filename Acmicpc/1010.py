def get_args():
    num_of_testcase = int(input())
    test_cases = []
    for _ in range(num_of_testcase):
        east_site, west_site = map(int, input().split())
        test_case = (east_site, west_site)
        test_cases.append(test_case)
    return num_of_testcase, test_cases


def solution(x):
    right, left = x
    denominator = 1
    numerator = 1
    for _ in range(right):
        denominator *= left
        numerator *= right
        right -= 1
        left -= 1
    return denominator // numerator


def main():
    num_test, test_cases = get_args()
    answer = []
    for test_case in test_cases:
        answer.append(solution(test_case))
    for i in range(num_test):
        print(answer[i])


if __name__ == '__main__':
    main()


