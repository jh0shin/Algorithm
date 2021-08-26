def solution(sales, links):
    from collections import defaultdict
    tree = defaultdict(list)
    dp = defaultdict(None)

    def f(k):
        inc, not_inc = sales[k-1], 0
        if k not in tree:
            dp[k] = (inc, not_inc)
            return dp[k]
        if k in dp: return dp[k]

        leaf, parent = [], []
        for v in tree[k]:
            t1, t2 = f(v)
            if v in tree: parent.append((t1, t2))
            else: leaf.append(t1)

        chk = False
        for p in parent:
            if p[0] < p[1]: chk = True
            not_inc += min(p)
        if chk == False:
            not_inc += min(leaf + [p[0]-p[1] for p in parent])

        dp[k] = (inc+sum(min(p) for p in parent), not_inc)
        return dp[k]

    for l in links:
        tree[l[0]].append(l[1])
    return min(f(1))

a = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
b = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]

if __name__=='__main__':
    print(solution(a, b))