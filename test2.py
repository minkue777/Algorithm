from itertools import combinations

def get_candidates(orders, num):
    candidates = []
    for order in orders:
        comb = list(combinations(order, num))
        candidates += comb
    return list(set(candidates))

def check_count(orders, candidate):
    count = 0
    for order in orders:
        count += all([c in order for c in candidate])
    return count

def solution(orders, course):
    orders = list(map(sorted, orders))
    total_ans = []
    for num in course:
        ans = []
        max_count = 2
        candidates = get_candidates(orders, num)
        for candidate in candidates:
            count = check_count(orders, candidate)
            if count > max_count:
                ans = []
                ans.append(''.join(candidate))
                max_count = count
            elif count == max_count:
                ans.append(''.join(candidate))
        total_ans += ans
    return sorted(total_ans, reverse=False)
        
print(solution(["XYZ", "XWY", "WXA"], [2]))