def solution(expression):
    from collections import deque
    from itertools import permutations
    import re
    q = deque()

    num = re.split('[+\-\*]', expression)
    exp = list(filter(lambda x: x != '', re.split('\d', expression)))
    l = []
    for i in range(len(exp)):
        l.append(num[i])
        l.append(exp[i])
    l.append(num[-1])

    ans = 0
    for pri in permutations('+-*', 3):
        postfix = []
        tmp = []
        for a in l:
            if a in '+-*':
                while tmp and pri.index(tmp[-1]) <= pri.index(a):
                    postfix.append(tmp.pop())
                tmp.append(a)
            else:
                postfix.append(a)
        while tmp: postfix.append(tmp.pop())
        
        tmp = []
        for p in postfix:
            if p in '+-*':
                y, x = tmp.pop(), tmp.pop()
                exec('tmp.append('+str(x)+p+str(y)+')')
            else: tmp.append(p)
        
        ans = max(ans, abs(tmp.pop()))
    
    return ans


a = "100-200*300-500+20"

if __name__=='__main__':
    print(solution(a))