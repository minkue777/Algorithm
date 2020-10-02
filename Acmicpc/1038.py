from itertools import combinations


def get_args() -> int:
    num = int(input())
    return num


def combination(left: int, right: int) -> int:
    if left - right < right:
        return combination(left, left - right)

    denominator = 1
    numerator = 1
    for _ in range(right):
        denominator *= left
        numerator *= right
        right -= 1
        left -= 1
    return denominator // numerator


def solution(n):
    # The number of decreasing numbers is 1023(1022th)
    if n >= 1023:
        return -1

    for i in range(1, 10):
        if n < combination(10, i):
            check_point = i
            break
        n -= combination(10, i)
    else:
        check_point = 10

    combination_list = combinations(range(10), check_point)
    sorted_combination_list = sorted([''.join(map(str, element[::-1])) for element in combination_list])
    return int(sorted_combination_list[n])


def main():
    n = get_args()
    nth_decreasing_number = solution(n)
    print(nth_decreasing_number)


if __name__ == '__main__':
    main()
