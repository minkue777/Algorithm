def get_args():
    popularity1, popularity2 = map(int, input().split())
    return popularity1, popularity2


def solution(p1: int, p2: int) -> int:
    return p2 - p1 if p2 > p1 else p1 - p2


def main():
    p1, p2 = get_args()
    print(solution(p1, p2))


if __name__ == '__main__':
    main()
