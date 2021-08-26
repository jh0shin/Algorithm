def solution(n, t, m, timetable):
    from collections import deque
    shuttle = 9 * 60
    timetable.sort()
    crew = deque([int(t.split(':')[0])*60+int(t.split(':')[1]) for t in timetable])
    ans = min(crew) - 1
    for i in range(n):
        if len(crew) < m: ans = shuttle
        elif crew[m-1] > shuttle: ans = shuttle
        else: ans = min(max(list(crew)[:m])-1, shuttle)
        for j in range(m):
            if len(crew) == 0 or crew[0] > shuttle: break
            else: crew.popleft()
        shuttle += t
    
    return f"{str(ans//60).zfill(2)}:{str(ans%60).zfill(2)}"

a = 2
b = 10
c = 2
d = ["09:10", "09:09", "08:00"]

if __name__=='__main__':
    print(solution(a, b, c, d))