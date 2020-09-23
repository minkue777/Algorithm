def solution(progress, speed):
    progress.reverse()
    speed.reverse()
    answer = []
    while progress:
        f = 100 - progress[-1]
        t = f // speed[-1] if f % speed[-1] == 0 else f // speed[-1] + 1
        d = [k*t for k in speed]
        
        progress = [k + d for k, d in zip(progress, d)]
        count = 0
        while progress and progress[-1] >= 100:
            progress.pop()
            speed.pop()
            count += 1
        answer.append(count)

    return answer

print(solution([95, 90, 99, 99, 80, 99], [2, 2, 2, 2, 2, 2]))