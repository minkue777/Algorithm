from typing import Tuple
from math import sqrt


def get_args():
    num_of_testcase = int(input())
    test_cases = []
    for _ in range(num_of_testcase):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        test_cases.append((x1, y1, r1, x2, y2, r2))
    return num_of_testcase, test_cases


def l2_distance(point1: Tuple[int, int], point2: Tuple[int, int]) -> float:
    """
    function for calculating Euclidean distance(l2 distance) between two points
    The x, y coordinates of two points are must be integer
    """
    x1, y1 = point1
    x2, y2 = point2
    distance_between_two_points: float = sqrt((x1-x2)**2 + (y1-y2)**2)
    return distance_between_two_points


def solution(test_case: Tuple[int, int, float, int, int, float]) -> int:
    x1, y1, r1, x2, y2, r2 = test_case
    # The number of solutions depends on the distance and radius between two points
    if (x1, y1) == (x2, y2):
        return -1 if r1 == r2 else 0
    distance: float = l2_distance((x1, y1), (x2, y2))
    if distance == abs(r1+r2) or distance == abs(r1-r2):
        return 1
    elif distance > abs(r1+r2) or distance < abs(r1-r2):
        return 0
    else:
        return 2


def main() -> None:
    num_of_testcase, test_cases = get_args()
    answer = []
    for test_case in test_cases:
        answer.append(solution(test_case))
    # print answer
    for ans in answer:
        print(ans)


if __name__ == "__main__":
    main()