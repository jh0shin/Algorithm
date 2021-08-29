def solution(k, num, links):
    import sys
    sys.setrecursionlimit(100001)

    def dfs(i, mid):
        if i == -1: return 0
        if num[i] > mid: return -1

        left = dfs(links[i][0], mid)
        right = dfs(links[i][1], mid)
        if left == -1 or right == -1: return -1

        if num[i]+left+right <= mid:
            return num[i]+left+right
        elif num[i]+left > mid and num[i]+right > mid:
            cnt[0] += 2
            return num[i]
        elif num[i]+left > mid and num[i]+right <= mid:
            cnt[0] += 1
            return num[i]+right
        elif num[i]+left <= mid and num[i]+right > mid:
            cnt[0] += 1
            return num[i]+left
        else:
            cnt[0] += 1
            return num[i]+min(left, right)

    findroot = [0 for _ in range(len(num)+1)]
    for a, b in links:
        findroot[a] += 1
        findroot[b] += 1
    root = findroot.index(0)
    
    l, r = max(num), 10**8+1
    while l < r:
        cnt = [1]
        mid = (l+r) // 2
        dfs(root, mid)
        # print(cnt, group, '|', l, r, mid)
        if cnt[0] <= k:
            r = mid
        else:
            l = mid+1
    
    return l

'''
# 채점 결과
# 정확성: 18.0
# 효율성: 7.0
# 합계: 25.0 / 100.0
def solution(k, num, links):
    def dfs(i, mid):
        if i == -1: return 0
        if num[i] > mid: return -1

        left = dfs(links[i][0], mid)
        right = dfs(links[i][1], mid)
        if left == -1 or right == -1: return -1

        if num[i]+left+right <= mid:
            cnt[1] = max(cnt[1], num[i]+left+right)
            return num[i]+left+right
        elif num[i]+left > mid and num[i]+right > mid:
            cnt[0] += 2
            cnt[1] = max(cnt[1], max(left, right))
            return num[i]
        elif num[i]+left > mid and num[i]+right <= mid:
            cnt[0] += 1
            cnt[1] = max(cnt[1], num[i]+right, left)
            return num[i]+right
        elif num[i]+left <= mid and num[i]+right > mid:
            cnt[0] += 1
            cnt[1] = max(cnt[1], num[i]+left, right)
            return num[i]+left
        else:
            cnt[0] += 1
            cnt[1] = max(cnt[1], num[i]+min(left, right))
            return num[i]+min(left, right)

    findroot = [0 for _ in range(len(num)+1)]
    for a, b in links:
        findroot[a] += 1
        findroot[b] += 1
    root = findroot.index(0)
    
    ans = 10**8
    l, r = 1, 10**8+1
    while l < r:
        cnt = [1, 0]
        mid = (l+r) // 2
        group = dfs(root, mid)
        # print(cnt, group, '|', l, r, mid)
        if cnt[0] == k and group != -1: ans = min(ans, cnt[1])
        if group != -1:
            r = mid
        else:
            l = mid+1
    
    return ans
'''

a = 2
b = [6, 9, 7, 5]
c = [[-1, -1], [-1, -1], [-1, 0], [2, 1]]

if __name__=='__main__':
    print(solution(a, b, c))