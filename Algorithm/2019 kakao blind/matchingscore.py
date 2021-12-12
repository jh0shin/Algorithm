'''
# 40 / 100
def solution(word, pages):
    import re
    from collections import defaultdict
    link = defaultdict(list)
    url = []
    basescore = [0 for _ in range(len(pages))]
    linknum = [0 for _ in range(len(pages))]

    for i, page in enumerate(pages):
        _url = re.search('<meta property="og:url" content=".*"/>', page, re.I|re.S).group()
        _url = _url.split()[2].split('"')[1]
        url.append(_url)

        links = re.findall('<a href=".*">', page)
        linknum[i] = len(links)
        for l in links:
            link[l.split('"')[1]].append(_url)

        body = re.sub('<.+?>', '', page)
        basescore[i] += len(re.findall('[\W|\d|_]+'+word+'[\W|\d|_]+', body, re.I))

    score = [i for i in basescore]
    for i, key in enumerate(url):
        for l in link[key]:
            score[i] += basescore[url.index(l)] / linknum[url.index(l)]
    
    return score.index(max(score))
'''

'''
# 80 / 100
# 1, 2, 9, 12 실패
# _word_word_ 와 같은 case에서 re.findall이 non-overapping이라 실패
def solution(word, pages):
    import re
    from collections import defaultdict
    link = defaultdict(list)
    url = []
    basescore = [0 for _ in range(len(pages))]
    linknum = [0 for _ in range(len(pages))]

    for i, page in enumerate(pages):
        _url = re.search('<meta property="og:url" content="\S*"/>', page, re.I|re.S).group()
        _url = _url.split()[2].split('"')[1]
        url.append(_url)

        links = re.findall('<a href="\S*">', page)
        linknum[i] = len(links)
        for l in links:
            link[l.split('"')[1]].append(_url)

        body = re.sub('<\S+?>', '', page)
        basescore[i] += len(re.findall('[\W|\d|_]+'+word+'[\W|\d|_]+', body, re.I))

    score = [i for i in basescore]
    for i, key in enumerate(url):
        for l in link[key]:
            score[i] += basescore[url.index(l)] / linknum[url.index(l)]
    
    return score.index(max(score))
'''

def solution(word, pages):
    import re
    from collections import defaultdict
    link = defaultdict(list)
    url = []
    basescore = [0 for _ in range(len(pages))]
    linknum = [0 for _ in range(len(pages))]

    for i, page in enumerate(pages):
        _url = re.search('<meta property="og:url" content="\S*"/>', page, re.I|re.S).group()
        _url = _url.split()[2].split('"')[1]
        url.append(_url)

        links = re.findall('<a href="\S*">', page)
        linknum[i] = len(links)
        for l in links:
            link[l.split('"')[1]].append(_url)

        body = re.sub('<\S+?>', '', page)
        basescore[i] += len(re.findall('(?<=[\W|\d|_])'+word+'(?=[\W|\d|_])', body, re.I))

    score = [i for i in basescore]
    for i, key in enumerate(url):
        for l in link[key]:
            score[i] += basescore[url.index(l)] / linknum[url.index(l)]
    
    return score.index(max(score))

a = 'blind'
b = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\n0Blind0Blind0 Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]

if __name__=='__main__':
    print(solution(a, b))