def solution(s):
    ans = len(s)
    for i in range(1, len(s)//2+1):
        b = ''
        cnt = 1
        r = ''
        for j in range(len(s)//i):
            if b == s[i*j:i*(j+1)]:
                cnt += 1
            elif cnt == 1:
                r += b
                b = s[i*j:i*(j+1)]
            else:
                r += str(cnt)+b
                b = s[i*j:i*(j+1)]
                cnt = 1
        if cnt == 1:
            r += b
            b = s[i*j:i*(j+1)]
        else:
            r += str(cnt)+b
            b = s[i*j:i*(j+1)]
            cnt = 1
        r += s[i*(j+1):]
        # print(i, r)
        if len(r) < ans: ans = len(r)
    return ans


a = "aabbaccc"

if __name__=='__main__':
    print(solution(a))