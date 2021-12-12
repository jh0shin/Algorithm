def solution(n, path, order):
    from collections import defaultdict, deque
    import sys
    sys.setrecursionlimit(10**6+1)
    tg = defaultdict(list)
    g = defaultdict(list)

    def dfs(r):
        # print(r, visited)
        visited[r] = 1
        log[r] = 1
        for adj in g[r]:
            if log[adj] == 0:
                if dfs(adj) == False:
                    return False
            if visited[adj] == 1:
                return False
        visited[r] = 0
        return True

    for s, e in path:
        tg[s].append(e)
        tg[e].append(s)
    q = deque([0])
    visited = [0 for _ in range(n)]
    visited[0] = 1
    while q:
        r = q.popleft()
        for adj in tg[r]:
            if visited[adj] == 0:
                visited[adj] = 1
                g[r].append(adj)
                q.append(adj)
    for s, e in order:
        g[s].append(e)

    visited = [0 for _ in range(n)]
    log = [0 for _ in range(n)]
    return dfs(0)

'''
# 채점 결과
# 정확성: 26.5
# 효율성: 30.5
# 합계: 57.0 / 100.0
def solution(n, path, order):
    from collections import defaultdict, deque
    tg = defaultdict(list)
    g = defaultdict(list)

    def dfs(r):
        visited[r] = 1
        log[r] = 1
        for adj in g[r]:
            if log[adj] == 1:
                if dfs(adj) == False:
                    return False
            if visited[r] == 1:             # 오류 : r => adj
                return False
        visited[r] = 0
        return True

    for s, e in path:
        tg[s].append(e)
        tg[e].append(s)
    q = deque([0])
    visited = [0 for _ in range(n)]
    visited[0] = 1
    while q:
        r = q.popleft()
        for adj in tg[r]:
            if visited[adj] == 0:
                visited[adj] = 1
                g[r].append(adj)
                q.append(adj)
    for s, e in order:
        g[s].append(e)

    visited = [0 for _ in range(n)]
    log = [0 for _ in range(n)]
    return dfs(0)
'''

'''
# 채점 결과
# 정확성: 41.2
# 효율성: 2.9       => 시간초과
# 합계: 44.1 / 100.0
def solution(n, path, order):
    from collections import defaultdict, deque
    tg = defaultdict(list)
    g = defaultdict(list)
    visited = [0 for _ in range(n)]
    path = deque(path)

    while path:
        s, e = path.popleft()
        if s == 0 or e == 0: g[max(s,e)].append(0)
        elif s in g: g[e].append(s)
        elif e in g: g[s].append(e)
        else: path.append([s, e])
    # for s, e in order: g[s].append(e)
    for s, e in order: g[e].append(s)
    # print(g)

    for i in range(n):
        if visited[i] == 0:
            tq = []
            tvisited = [0 for _ in range(n)]
            tvisited[i] = 1
            tq.append(i)
            while tq:
                r = tq.pop()
                # print(r)
                for adj in g[r]:
                    if tvisited[adj] == 0:
                        tvisited[adj] = 1
                        tq.append(adj)
                    elif adj == i:
                        # print(i, r, g[r], adj)
                        return False
        for i in range(n):
            if tvisited[i] == 1: visited[i] = 1
    
    return True
'''


a = 9
b = [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]]
c = [[4,1],[8,7],[6,5]]

if __name__=='__main__':
    print(solution(a, b, c))