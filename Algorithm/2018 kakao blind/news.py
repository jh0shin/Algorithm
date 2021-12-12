from collections import deque
def solution(str1, str2):
    s1, s2 = [], []
    jac = {}
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            s1.append(str1[i:i+2].lower())
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            s2.append(str2[i:i+2].lower())
    
    inter = 0
    uni = 0
    s1.sort()
    s2.sort()
    s1 = deque(s1)
    s2 = deque(s2)

    # print(s1, s2)
    while len(s1) != 0 or len(s2) != 0:
        if len(s1) == 0:
            s2.popleft()
        elif len(s2) == 0:
            s1.popleft()
        else:
            if s1[0] == s2[0]:
                inter += 1
                s1.popleft()
                s2.popleft()
            elif s1[0] < s2[0]:
                s1.popleft()
            else:
                s2.popleft()
        uni += 1

    if uni == 0: return 65536
    else: return int(inter / uni * 65536)


a = 'FRANCE'
b = 'french'

if __name__=='__main__':
    print(solution(a, b))