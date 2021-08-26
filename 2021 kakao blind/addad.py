'''
# 시간초과
def solution(play_time, adv_time, logs):
    def f(time):
        t = list(map(int, time.split(':')))
        return t[0]*3600 + t[1]*60 + t[2]

    start, end, section = [], [], []
    play_time, adv_time = f(play_time), f(adv_time)

    for log in logs:
        s, e = map(lambda x: f(x), log.split('-'))
        start.append(s)
        end.append(e)
        section.append((s, e))
    
    ans = 0
    # _max = len([s for s in start if s < adv_time])
    _max = 0

    for s in start:
        cnt = 0
        for sec in section:
            if sec[0] <= s < sec[1] or sec[0] < s + adv_time < sec[1] or sec[1] - adv_time < s <= sec[0]:
                cnt += 1
        if cnt == _max and s < ans:
            ans = s
        if cnt > _max:
            _max = cnt
            ans = s

    for e in end:
        cnt = 0
        for sec in section:
            if sec[0] <= e - adv_time < sec[1] or sec[0] < e < sec[1] or sec[1] < e <= sec[0] + adv_time:
                cnt += 1
        if cnt == _max and e - adv_time < ans:
            ans = e - adv_time
        if cnt > _max:
            _max = cnt
            ans = e - adv_time

    ans = min(ans, play_time - adv_time)
    return ':'.join([str(ans//3600).zfill(2), str((ans%3600)//60).zfill(2), str(ans%60).zfill(2)])
'''

'''
# 64.5 / 100 (시간 초과)
def solution(play_time, adv_time, logs):
    def f(time):
        t = list(map(int, time.split(':')))
        return t[0]*3600 + t[1]*60 + t[2]

    play_time, adv_time = f(play_time), f(adv_time)
    dp = [0 for _ in range(play_time+1)]

    for log in logs:
        s, e = map(lambda x: f(x), log.split('-'))
        for i in range(s, e): dp[i] += 1
    
    ans = 0
    tmp = _max = sum(dp[:adv_time])
    for i in range(play_time - adv_time):
        tmp += dp[i+adv_time] - dp[i]
        if tmp > _max:
            _max = tmp
            ans = i + 1
    return ':'.join([str(ans//3600).zfill(2), str((ans%3600)//60).zfill(2), str(ans%60).zfill(2)])
'''

def solution(play_time, adv_time, logs):
    def f(time):
        t = list(map(int, time.split(':')))
        return t[0]*3600 + t[1]*60 + t[2]

    play_time, adv_time = f(play_time), f(adv_time)
    dp = [0 for _ in range(play_time+1)]
    chk = [0 for _ in range(play_time+1)]

    for log in logs:
        s, e = map(lambda x: f(x), log.split('-'))
        chk[s] += 1
        chk[e] -= 1
    
    dp[0] = chk[0]
    for i in range(1, play_time+1):
        dp[i] = dp[i-1] + chk[i]
        # for i in range(s, e): dp[i] += 1
    
    ans = 0
    tmp = _max = sum(dp[:adv_time])
    for i in range(play_time - adv_time):
        tmp += dp[i+adv_time] - dp[i]
        if tmp > _max:
            _max = tmp
            ans = i + 1
    return ':'.join([str(ans//3600).zfill(2), str((ans%3600)//60).zfill(2), str(ans%60).zfill(2)])

a = "99:59:59"
b = "25:00:00"
c = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]

if __name__=='__main__':
    print(solution(a, b, c))