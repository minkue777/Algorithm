def get_args():
    length = int(input())
    array = list(map(int, input().split()))
    return length, array


def solution(length, array):
    ans = [0] * length
    array_with_idx = list(enumerate(array))
    rank = sorted(array_with_idx, key=lambda x: x[1])
    for i in range(length):
        ans[rank[i][0]] = i
    for i in range(length):
        print(ans[i], end=' ')


if __name__ == '__main__':
    n, input_array = get_args()
    solution(n, input_array)
