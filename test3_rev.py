def get_score(info):
    ans = 0
    if info[0] == 'cpp':
        ans += 1 * (10**8)
    elif info[0] == 'java':
        ans += 2 * (10**8)
    else:
        ans += 3 * (10**8)
    
    if info[1] == 'backend':
        ans += 1 * (10**7)
    else:
        ans += 2 * (10**7)
    
    if info[2] == 'junior':
        ans += 1 * (10**6)
    else:
        ans += 2 * (10**6)
    
    if info[3] == 'chicken':
        ans += 1 * (10**5)
    else:
        ans += 2 * (10**5)
    
    return ans + info[4]

def get_records(info):
    records = []
    for record in info:
        record = record.split()
        record.append(int(record.pop()))
        records.append(record)
    records = sorted(records, key = get_score)
    return records

def get_queries(query):
    queries = []
    for q in query:
        ans = q.split(' and ')
        soul_food, criterion = ans.pop().split()
        ans += [soul_food, int(criterion)]
        queries.append(ans)
    return queries

def check(records, query):
    start = 0
    end = len(records) - 1
    while start <= end:
        mid = (start + end ) // 2
        if get_score(records[mid]) < get_score(query):
            start = mid+1
        elif get_score(records[mid]) > get_score(query):
            end = mid-1
        else:
            return mid
    return end
    
def solution(info, query):
    records = get_records(info)
    queries = get_queries(query)
    ans = []
    for query in queries:
        ans.append(check(records, query))
    return ans


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80", "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]

records = get_records(info)
queries = get_queries(query)

print(records)
print(check(records, queries[5]))

