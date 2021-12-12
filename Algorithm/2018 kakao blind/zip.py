def solution(msg):
    dic = {}
    ans = []
    tmp = ''
    for i in range(26):
        dic[chr(ord('A')+i)] = i+1
    i = 0
    while 1:
        tmp += msg[i]
        if i == len(msg)-1:
            ans.append(dic[tmp])
            break
        elif tmp+msg[i+1] not in dic.keys():
            ans.append(dic[tmp])
            dic[tmp+msg[i+1]] = len(dic)+1
            tmp = ''
            i += 1
        elif tmp+msg[i+1] in dic.keys():
            i += 1
        # print(tmp, ans)
    
    return ans

a = 'TOBEORNOTTOBEORTOBEORNOT'

if __name__=='__main__':
    print(solution(a))