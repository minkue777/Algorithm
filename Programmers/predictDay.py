def calRemainder(m, d):
    firstDay = {1: 0, 2: 3, 3: 4, 4: 0, 5: 2, 6: 5, 7: 0, 8: 3, 9: 6, 10: 1, 11: 4, 12:6}
    return (firstDay[m] + d + 4) % 7

def solution(m, d):
    dayList = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    Day = {idx: day for idx, day in enumerate(dayList)}
    remainder = calRemainder(m, d)
    return Day[remainder]

print(solution(5, 24))







