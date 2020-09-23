def log2int(logs):
    ans = []
    for log in logs:
        start_time = 0
        end_time = 0
        try:
            start, end = log.split('-')
            h, m, s = start.split(':')
            start_time = int(h)*3600 + int(m)*60 + int(s)
            h, m, s = end.split(':')
            end_time = end_time = int(h)*3600 + int(m)*60 + int(s)
            ans.append((start_time, end_time))
        except:
            h, m, s = logs.split(':')
            return int(h)*3600 + int(m)*60 + int(s)
    return ans

def int2log(time):
    h = time // 3600
    time %= 3600
    m = time // 60
    s = time % 60
    return '{}:{}:{}'.format(str(h).rjust(2, '0'), str(m).rjust(2, '0'), str(s).rjust(2, '0'))

def cal_time(start_time, adv_time, logs):
    ans = 0
    for log in logs:
        if start_time+adv_time < log[0] or start_time > log[1]:
            return ans
        ans += min(start_time + adv_time, log[1]) - max(start_time, log[0])
    return ans
    
def solution(play_time, adv_time, logs):
    play_time = log2int(play_time)
    adv_time = log2int(adv_time)    
    logs = log2int(logs)
    max_time = 0
    ans = 0
    
    target_point1 = [x for x, y in logs]
    target_point2 = [y-adv_time for x, y in logs if y-adv_time >= 0]
    target_point = [0] + sorted(target_point1 + target_point2)  
    
    for start_time in range(play_time - adv_time + 1):
        time = 0
        end_time = start_time + adv_time
        for log in logs:
            if end_time < log[0]:
                continue
            if start_time > log[1]:
                continue
            time += min(end_time, log[1]) - max(start_time, log[0])
            
        if time > max_time:
            ans = start_time
            max_time = time
            
    return int2log(ans)
            
play_time = "50:00:00"	
adv_time = "50:00:00"	
logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]

print(solution(play_time, adv_time, logs))
