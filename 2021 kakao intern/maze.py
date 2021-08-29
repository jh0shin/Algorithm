def solution(n, start, end, roads, traps):
    import heapq
    from collections import defaultdict
    # dist = {i: {j: float('inf') for j in range(2**len(traps))} for i in range(n+1)}
    dist = [[float('inf') for j in range(2**len(traps))] for i in range(n+1)]
    trap = {t: i for i, t in enumerate(traps)}
    path = defaultdict(list)

    q = []
    ans = float('inf')
    dist[start][0] = 0
    heapq.heappush(q, [dist[start][0], 0, start])

    for s, e, v in roads:
        path[s].append([e, v, 0])
        path[e].append([s, v, 1])

    while q:
        d, state, cur = heapq.heappop(q)
        if cur == end: ans = min(ans, d)
        if dist[cur][state] < d: continue

        for adj, v, s in path[cur]:
            cnt = 0
            if cur in traps: cnt += 1&(state>>trap[cur])
            if adj in traps: cnt += 1&(state>>trap[adj])
            if cnt % 2 != s: continue
            # print('---', d, state, cur, ':', adj, v, s)
            newstate = state
            if adj in traps:
                newstate = (1<<trap[adj])^state
            if d+v < dist[adj][newstate]:
                dist[adj][newstate] = d+v
                heapq.heappush(q, [d+v, newstate, adj])
    
    return ans

'''
# 64.1
# 시간 초과가 많음
def solution(n, start, end, roads, traps):
    import heapq
    from collections import defaultdict
    dist = {i: {bin(j)[2:].zfill(len(traps)): 10**21 for j in range(2**len(traps))} for i in range(n+len(traps))}
    path = defaultdict(dict)
    traps = [t-1 for t in traps]

    q = []
    dist[start-1]['0'*len(traps)] = 0
    heapq.heappush(q, [dist[start-1]['0'*len(traps)], ['0' for _ in range(len(traps))], start-1])

    for s, e, v in roads:
        s, e = s-1, e-1
        if e in path[s]: path[s][e] = min(path[s][e], v)
        else:            path[s][e] = v
        if s in path[-e]: path[-e][s] = min(path[-e][s], v)
        else:             path[-e][s] = v

    while q:
        # print(q)
        d, state, cur = heapq.heappop(q)
        # print(d, cur)
        if dist[cur][''.join(state)] < d: continue

        for adj, v in path[cur].items():
            cnt = 0
            if cur in traps: cnt += int(state[traps.index(cur)])
            if adj in traps: cnt += int(state[traps.index(adj)])
            if cnt % 2 == 1: continue
            # print('---', cur, adj, d, v, cnt)
            newd = d + v
            newstate = [_ for _ in state]
            if adj in traps:
                newstate[traps.index(adj)] = '0' if newstate[traps.index(adj)] == '1' else '1'
            if newd < dist[adj][''.join(newstate)]:
                dist[adj][''.join(newstate)] = newd
                heapq.heappush(q, [newd, newstate, adj])

        for adj, v in path[-cur].items():
            cnt = 0
            if cur in traps: cnt += int(state[traps.index(cur)])
            if adj in traps: cnt += int(state[traps.index(adj)])
            if cnt % 2 == 0: continue
            # print('---', cur, adj, d, v, cnt)
            newd = d + v
            newstate = [_ for _ in state]
            if adj in traps:
                newstate[traps.index(adj)] = '0' if newstate[traps.index(adj)] == '1' else '1'
            if newd < dist[adj][''.join(newstate)]:
                dist[adj][''.join(newstate)] = newd
                heapq.heappush(q, [newd, newstate, adj])
    
    # print(dist)
    # print(path)
    return min(dist[end-1].values())
'''

'''
# 66.7 / 100
# 3, 5, 6, 7, 8, 9, 10 오답
def solution(n, start, end, roads, traps):
    import heapq
    from collections import defaultdict
    dist = {i: 10**21 for i in range(n+len(traps))}
    trap = {t-1: n+i for i, t in enumerate(traps)}
    trap.update({n+i: t-1 for i, t in enumerate(traps)})
    path = defaultdict(dict)
    print(dist, trap)

    q = []
    dist[start-1] = 0
    heapq.heappush(q, [dist[start-1], start-1])

    for s, e, v in roads:
        s, e = s-1, e-1
        if e in path[s]: path[s][e] = min(path[s][e], v)
        else:            path[s][e] = v

        if s in trap:
            ts = trap[s]
            if ts in path[e]: path[e][ts] = min(path[e][ts], v)
            else:            path[e][ts] = v
        if e in trap:
            te = trap[e]
            if s in path[te]: path[te][s] = min(path[te][s], v)
            else:            path[te][s] = v

    while q:
        d, cur = heapq.heappop(q)
        print(d, cur)
        if dist[cur] < d: continue

        for adj, v in path[cur].items():
            print('---', v, adj)
            newd = d + v
            if newd < dist[adj]:
                dist[adj] = newd
                if adj in trap: heapq.heappush(q, [newd, trap[adj]])
                else:           heapq.heappush(q, [newd, adj])
    
    print(dist)
    print(path)
    return dist[end-1]
'''

'''
# 오답
def solution(n, start, end, roads, traps):
    path = [[10**6 for _ in range(n)] for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    ans = []

    def f(s, e, r):
        # print(s, e, r, path, visited)
        if s == e:
            ans.append(r)
            return

        for p, v in enumerate(path[s]):
            if visited[s][p] == 0 and path[s][p] != 10**6:
                visited[s][p] = 1
                if p+1 in traps:
                    for i in range(n):
                        tmp = path[p][i]
                        path[p][i] = path[i][p]
                        path[i][p] = tmp
                # print(p, e, r+v)
                f(p, e, r+v)
                if p+1 in traps:
                    for i in range(n):
                        tmp = path[p][i]
                        path[p][i] = path[i][p]
                        path[i][p] = tmp
                visited[s][p] = 0

    for s, d, v in roads:
        path[s-1][d-1] = min(path[s-1][d-1], v)
    f(start-1, end-1, 0)
    return min(ans)
'''                

a = 4
b = 1
c = 4
d = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
e = [2, 3]

if __name__=='__main__':
    print(solution(a, b, c, d, e))