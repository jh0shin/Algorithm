'''
# 92 / 100
def solution(n, weak, dist):
    from itertools import permutations
    _weak = [w for w in weak]
    _weak += [w+n for w in weak]
    
    for i in range(len(dist)):
        for j in range(len(weak)):
            permut = list(permutations(dist, i))
            for per in permut:
                cpy = [w for w in _weak[j:j+len(weak)]]
                for p in per:
                    # print(p, per, permut, cpy)
                    if cpy == []: break
                    start = cpy[0]
                    while cpy != [] and cpy[0] <= start+p: cpy.pop(0)
                if cpy == []:
                    # print(per)
                    return i
    
    return -1
'''

def solution(n, weak, dist):
    from itertools import permutations
    _weak = [w for w in weak]
    _weak += [w+n for w in weak]
    
    for i in range(1, len(dist)+1):
        for j in range(len(weak)):
            permut = list(permutations(dist, i))
            for per in permut:
                cpy = [w for w in _weak[j:j+len(weak)]]
                for p in per:
                    # print(p, per, permut, cpy)
                    if cpy == []: break
                    start = cpy[0]
                    while cpy != [] and cpy[0] <= start+p: cpy.pop(0)
                if cpy == []:
                    # print(per)
                    return i
    
    return -1

# a = 12
# b = [1, 3, 4, 9, 10]
# c = [3, 5, 7]

a = 200
b = [0, 100]
c = [1, 1]

if __name__=='__main__':
    print(solution(a, b, c))