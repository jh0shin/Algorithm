'''
# 런타임 에러 (1,6,7,9,13,23,24,25)
def solution(N, stages):
    now = [stages.count(i+1) for i in range(N+1)]
    failrate = [0 if sum(now[i:]) == 0 else (now[i]/sum(now[i:]), -i-1) for i in range(N)]
    failrate.sort(reverse=True)
    ans = [-f[1] for f in failrate]
    return ans
'''

'''
# 실패 (1,6,7,9,13,23,24,25)
def solution(N, stages):
    now = [0 for _ in range(N+1)]
    for s in stages: now[s-1] += 1
    acc = now[N]
    failrate = [(0, 0) for _ in range(N)]
    for i in range(N):
        acc += now[N-1-i]
        if acc == 0: (0, i-N)
        else: failrate[N-1-i] = (now[N-1-i]/acc, i-N)
    failrate.sort(reverse=True)
    ans = [-f[1] for f in failrate]
    return ans
'''

'''
# 비효율적 정답
def solution(N, stages):
    now = [stages.count(i+1) for i in range(N+1)]
    failrate = [(0, -i-1) if sum(now[i:]) == 0 else (now[i]/sum(now[i:]), -i-1) for i in range(N)]
    failrate.sort(reverse=True)
    ans = [-f[1] for f in failrate]
    return ans
'''

# 정답
def solution(N, stages):
    now = [0 for _ in range(N+1)]
    for s in stages: now[s-1] += 1
    acc = now[N]
    failrate = [(0, -i-1) for i in range(N)]
    for i in range(N):
        acc += now[N-1-i]
        if acc == 0: pass
        else: failrate[N-1-i] = (now[N-1-i]/acc, i-N)
    failrate.sort(reverse=True)
    print(failrate)
    ans = [-f[1] for f in failrate]
    return ans

a = 5
b = [2, 1, 2, 2, 4, 3, 3]

if __name__=='__main__':
    print(solution(a, b))