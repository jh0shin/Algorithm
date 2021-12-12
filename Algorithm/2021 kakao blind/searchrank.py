def solution(info, query):
    from collections import defaultdict
    dic = {'java': '0', 'python': '1', 'cpp':'2',
           'backend': '0', 'frontend': '1',
           'junior': '0', 'senior': '1',
           'pizza': '0', 'chicken': '1'}
    db = defaultdict(list)
    ans = []

    for apply in info:
        db[''.join(map(lambda x: dic[x], apply.split()[:4]))].append(int(apply.split()[-1]))

    for key in db:
        db[key].sort()

    for qry in query:
        score = int(qry.split()[-1])
        tmp = []
        lang, part, career, food = ''.join(qry.split()[:-1]).split('and')
        tmp.append(['0', '1', '2']) if lang == '-' else tmp.append([dic[lang]])
        tmp.append(['0', '1']) if part == '-' else tmp.append([dic[part]])
        tmp.append(['0', '1']) if career == '-' else tmp.append([dic[career]])
        tmp.append(['0', '1']) if food == '-' else tmp.append([dic[food]])

        keys = []
        for a in tmp[0]:
            for b in tmp[1]:
                for c in tmp[2]:
                    for d in tmp[3]:
                        keys.append(''.join([a, b, c, d]))
        
        cnt = 0
        for key in keys:
            if key not in db.keys(): continue
            # cnt += len([v for v in db[key] if v >= score])

            l, r = 0, len(db[key])
            while l < r:
                mid = (l+r)//2
                if db[key][mid] >= score:
                    r = mid
                else:
                    l = mid + 1
            cnt += len(db[key]) - l

        ans.append(cnt)
    
    return ans


a = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
b = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

if __name__=='__main__':
    print(solution(a, b))