def get_args():
    N = int(input("동전 개수 입력 : "))
    coins = list(map(int, input("동전 단위 입력 : ").split()))
    return N, coins

N, coins = get_args()
coins.sort()

def solution(coins):
    target = 1
    for c in coins:
        if target < c:
            break
        target += c
    return target

print(solution(coins))


