def solution(s):
    from collections import defaultdict
    import re
    d = defaultdict(int)
    s = list(filter(lambda x: x!='', re.split('[{,}]', s)))
    for t in s:
        d[t] += 1
    r = sorted(d.items(), key=lambda x: -x[1])
    return [int(t[0]) for t in r]

a = "{{2},{2,1},{2,1,3},{2,1,3,4}}"

if __name__=='__main__':
    print(solution(a))