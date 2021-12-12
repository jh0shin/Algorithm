def solution(k, room_number):
    import sys
    sys.setrecursionlimit(10**6)
    next = {}

    def f(n):
        if n not in next:
            next[n] = n + 1
            return n
        else:
            next[n] = f(next[n]) + 1
            return next[n] - 1

    return [f(r) for r in room_number]

'''
# 채점 결과
# 정확성: 78.8
# 효율성: 12.1
# 합계: 90.9 / 100.0
def solution(k, room_number):
    ans = []
    next = {}

    for r in room_number:
        if r not in next:
            ans.append(r)
            next[r] = r + 1     
        else:
            tmp = next[r]
            try:
                while 1:
                    tmp = next[tmp]
            except:
                ans.append(tmp)
                next[r] = tmp + 1
                next[tmp] = tmp + 1
            # print(tmp)
        # print(next, ans)
    
    return ans
'''

'''
# 채점 결과
# 정확성: 78.8
# 효율성: 3.0
# 합계: 81.8 / 100.0
def solution(k, room_number):
    ans = []
    next = {}

    for r in room_number:
        if r not in next:
            ans.append(r)
            next[r] = r + 1   
        elif next[r] not in next:
            ans.append(next[r])
            next[next[r]] = next[r] + 1
            next[r] += 1     
        else:
            while next[r] in next:
                next[r] = next[next[r]]
            ans.append(next[r])
            next[next[r]] = next[r] + 1
            # print(tmp)
        # print(next, ans)
    
    return ans
'''

a = 10
b = [1,3,4,1,3,1]

if __name__=='__main__':
    print(solution(a, b))