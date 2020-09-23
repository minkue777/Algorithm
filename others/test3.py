def get_records(info):
    records = []
    for record in info:
        record = record.split()
        record.append(int(record.pop()))
        records.append(record)
    records = sorted(records, key = lambda x : (x[0], x[1], x[2], x[3], x[4]))
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
    ans = records
    ans = [record for record in ans if query[0] == '-' or record[0] == query[0]]
    ans = [record for record in ans if query[1] == '-' or record[1] == query[1]]
    ans = [record for record in ans if query[2] == '-' or record[2] == query[2]]
    ans = [record for record in ans if query[3] == '-' or record[3] == query[3]]
    ans = [record for record in ans if record[4] >= query[4]]
    return len(ans)
    
def solution(info, query):
    records = get_records(info)
    queries = get_queries(query)
    ans = []
    for query in queries:
        ans.append(check(records, query))
    return ans


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80", "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]

print(solution(info, query))

