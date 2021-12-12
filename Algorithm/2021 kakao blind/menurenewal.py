def solution(orders, course):
    from itertools import combinations
    from collections import defaultdict

    num = {}
    ans = []
    for c in course:
        num[c] = defaultdict(int)
    for order in orders:
        for c in course:
            menu = list(combinations(order, c))
            for m in menu:
                num[c][''.join(sorted(m))] += 1
    for c in course:
        if len(num[c]) == 0: continue
        maximum = max(num[c].items(), key=lambda x: x[1])[1]
        if maximum == 1: continue
        for i in num[c]:
            if num[c][i] == maximum: ans.append(i)
    ans.sort()

    return ans

a = ["XYZ", "XWY", "WXA"]
b = [2, 3, 4]

if __name__=='__main__':
    print(solution(a, b))