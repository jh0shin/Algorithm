'''
# 60 / 100
def solution(p):
    def f(s):
        if s == '': return ''
        u = s[:2]
        v = s[2:]
        for i in range(2, len(s), 2):
            u = s[:i]
            v = s[i:]
            if u.count('(') == u.count(')'):
                break

        # print(u, '||', v)
        tmp = u
        while tmp.count('()') != 0:
            tmp = tmp.replace('()', '')
        if tmp == '': return u+f(v)

        u = u[1:-1]
        u = u.replace('(', '@').replace(')', '(').replace('@', ')')
        return '('+f(v)+')'+u
    
    return f(p)
'''

'''
# 76 / 100
def solution(p):
    def f(s):
        if s == '': return ''
        tmp = s
        while tmp.count('()') != 0:
            tmp = tmp.replace('()', '')
        if tmp == '': return s

        u = s[:2]
        v = s[2:]
        for i in range(2, len(s), 2):
            u = s[:i]
            v = s[i:]
            if u.count('(') == u.count(')'):
                break

        # print(u, '||', v)
        tmp = u
        while tmp.count('()') != 0:
            tmp = tmp.replace('()', '')
        if tmp == '': return u+f(v)

        u = u[1:-1]
        u = u.replace('(', '@').replace(')', '(').replace('@', ')')
        return '('+f(v)+')'+u
    
    return f(p)
'''

def solution(p):
    def f(s):
        if s == '': return ''

        u = s[:2]
        v = s[2:]
        for i in range(2, len(s)+1, 2):
            u = s[:i]
            v = s[i:]
            if u.count('(') == u.count(')'):
                break

        # print(u, '||', v)
        tmp = u
        while tmp.count('()') != 0: tmp = tmp.replace('()', '')
        if tmp == '': return u+f(v)

        u = u[1:-1]
        u = u.replace('(', '@').replace(')', '(').replace('@', ')')
        return '('+f(v)+')'+u
    
    return f(p)

a = "()))((()"

if __name__=='__main__':
    print(solution(a))