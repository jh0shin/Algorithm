def solution(lines):
    time = []
    pos = []
    for l in lines:
        t = l.split(' ')[1].split(':')
        end = int(t[0]) * 3600000 + int(t[1]) * 60000 + int(''.join(t[2].split('.')))
        start = end - int(float(l.split(' ')[2].rstrip('s')) * 1000) + 1
        time.append([start, end])
        pos.append(start)
        pos.append(end)
    pos.sort()
    # print(time, pos)

    ans = 0
    for f in pos:
        cnt = 0
        for t in time:
            if f <= t[0] <= f + 999 or f <= t[1] <= f + 999 or t[0] <= f <= t[1] - 999:
                cnt += 1
        # print(f, cnt)
        if ans < cnt:
            ans = cnt

    for r in pos:
        cnt = 0
        for t in time:
            if r - 999 <= t[0] <= r or r - 999 <= t[1] <= r or t[0] + 999 <= r <= t[1]:
                cnt += 1
        # print(r, cnt)
        if ans < cnt:
            ans = cnt
    
    return ans
        


a = 	["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]

if __name__=='__main__':
    print(solution(a))