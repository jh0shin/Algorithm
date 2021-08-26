def solution(words, queries):
    from collections import defaultdict
    ftrie = {}
    btrie = {}
    wordnum = defaultdict(int)

    for word in words:
        f = ftrie
        b = btrie
        for i in range(len(word)):
            if word[i] not in f:
                f[word[i]] = [[], {}]
            f[word[i]][0].append(len(word)-i-1)
            f = f[word[i]][1]
            if word[-i-1] not in b:
                b[word[-i-1]] = [[], {}]
            b[word[-i-1]][0].append(len(word)-i-1)
            b = b[word[-i-1]][1]
        wordnum[len(word)] += 1
    
    ans = []
    for query in queries:
        isfind = True
        if query.count('?') == len(query):
            ans.append(wordnum[len(query)])
            # tmp = 0
            # for key in ftrie:
            #     tmp += ftrie[key][0].count(len(query)-1)
            # ans.append(tmp)
        elif query[-1] == '?':
            tstr = query.split('?')[0]
            f = ftrie
            for i in range(len(tstr)-1):
                if tstr[i] not in f:
                    isfind = False
                    break
                f = f[tstr[i]][1]
            if isfind and tstr[-1] in f: ans.append(f[tstr[-1]][0].count(query.count('?')))
            else: ans.append(0)
        elif query[0] == '?':
            tstr = query.split('?')[-1]
            b = btrie
            for i in range(len(tstr)-1):
                if tstr[-i-1] not in b:
                    isfind = False
                    break
                b = b[tstr[-i-1]][1]
            if isfind and tstr[0] in b: ans.append(b[tstr[0]][0].count(query.count('?')))
            else: ans.append(0)
    return ans
    

a = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
b = ["fro??", "????o", "fr???", "fro???", "pro?"]

if __name__=='__main__':
    print(solution(a, b))