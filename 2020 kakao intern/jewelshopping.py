def solution(gems):
    from collections import defaultdict
    gem = len(set(gems))
    cnt = defaultdict(int)
    ans = []

    l, r = 0, -1
    while l < len(gems) and r < len(gems):
        # print(l+1, r+1, cnt, len(cnt))
        if len(cnt) < gem:
            r += 1
            if r >= len(gems): break
            cnt[gems[r]] += 1
        else:
            ans.append([l+1, r+1])
            cnt[gems[l]] -= 1
            if cnt[gems[l]] == 0:
                cnt.pop(gems[l])
            l += 1
    ans.sort(key=lambda x: (x[1]-x[0], x[0]))

    return ans[0]
    

'''
# 채점 결과
# 정확성: 33.3
# 효율성: 44.4
# 합계: 77.8 / 100.0
def solution(gems):
    gem = len(set(gems))
    pos = dict()
    a = []

    for i, g in enumerate(gems):
        pos[g] = i
        if len(pos) == gem: a.append((min(pos.values())+1, max(pos.values())+1))
    a.sort(key=lambda x: (x[1]-x[0], x[0]))

    return a[0]
'''

'''
# 채점 결과
# 정확성: 33.3
# 효율성: 4.4
# 합계: 37.8 / 100.0
def solution(gems):
    gem = set(gems)
    ret = (len(gems), 1)

    l, r = 1, 10**5
    while l < r:
        mid = (l+r) // 2
        ans = -1
        if len(gems) < mid:
            r = mid
            continue
        for i in range(len(gems)-mid+1):
            if len(gem) == len(set(gems[i:i+mid])):
                ans = i
                break
        if ans != -1:
            r = mid
            ret = min(ret, (mid, i+1))
        else:
            l = mid + 1
    
    return [ret[1], sum(ret)-1]
'''

a = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

if __name__=='__main__':
    print(solution(a))