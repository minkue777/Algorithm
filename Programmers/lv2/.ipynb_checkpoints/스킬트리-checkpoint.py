def solution(skill, skill_trees):
    count = 0
    for st in skill_trees:
        order = []
        for s in skill:
            order.append(st.find(s))
    
        order = [100 if x == -1 else x for x in order]
        print(order, sorted(order))
        if order == sorted(order):
            count += 1
    return count

print(solution("CBD", ["CBAE", "CBDA"]))