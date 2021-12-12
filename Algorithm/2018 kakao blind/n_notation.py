def solution(n, t, m, p):
    ans = []
    string = ''
    chk = '0123456789ABCDEF'
    num = 0
    while len(ans) != t:
        tmp = []
        k = num
        while k != 0:
            tmp.append(chk[k%n])
            k //= n
        tmp = [tmp[len(tmp)-1-i] for i in range(len(tmp))]
        if tmp == []: tmp.append('0')
        string += ''.join(tmp)
        # print(ans, string, tmp)
        while len(string) >= m:
            ans.append(string[p-1])
            string = string[m:]
            
        num += 1
    
    return ''.join(ans)

a = 16
b = 16
c = 2
d = 2

if __name__=='__main__':
    print(solution(a, b, c, d))