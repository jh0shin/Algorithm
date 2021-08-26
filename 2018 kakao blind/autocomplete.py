def solution(words):
    dic = {}
    for w in words:
        r = dic
        for t in w:
            if t not in r:
                r[t] = [0, {}]
            r[t][0] += 1
            r = r[t][1]
        # r[1]['*'] = True

    ans = 0
    for w in words:
        r = dic
        for i in range(len(w)):
            # print(r)
            if r[w[i]][0] == 1:
                break
            r = r[w[i]][1]
        ans += i+1
        # print(i+1)

    return ans


a = ["abc","def","ghi","jklm"]

if __name__=='__main__':
    print(solution(a))