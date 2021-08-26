def solution(board, r, c):
    from collections import defaultdict
    from itertools import permutations

    def bfs(x, y, a, b):
        queue = [(x, y)]
        ret = 0
        while queue:
            if (a, b) in queue: return ret
            ret += 1
            next = set()
            for q in queue:
                if q[0]+1 in range(0, 4):
                    next.add((q[0]+1, q[1]))
                if q[0]-1 in range(0, 4):
                    next.add((q[0]-1, q[1]))
                if q[1]+1 in range(0, 4):
                    next.add((q[0], q[1]+1))
                if q[1]-1 in range(0, 4):
                    next.add((q[0], q[1]-1))
                for i in range(1, 4):
                    if q[0]+i == 3 or (q[0]+i in range(0, 4) and board[q[0]+i][q[1]] != 0):
                        next.add((q[0]+i, q[1]))
                        break
                for i in range(1, 4):
                    if q[0]-i == 0 or (q[0]-i in range(0, 4) and board[q[0]-i][q[1]] != 0):
                        next.add((q[0]-i, q[1]))
                        break
                for i in range(1, 4):
                    if q[1]+i == 3 or (q[1]+i in range(0, 4) and board[q[0]][q[1]+i] != 0):
                        next.add((q[0], q[1]+i))
                        break
                for i in range(1, 4):
                    if q[1]-i == 0 or (q[1]-i in range(0, 4) and board[q[0]][q[1]-i] != 0):
                        next.add((q[0], q[1]-i))
                        break
            queue = list(next)
        return -1

    def f(x, y, per, index, dist):
        if index == len(per): 
            ans.append(dist)
            return

        cards = pos[per[index]]
        d = bfs(x, y, cards[0][0], cards[0][1]) + bfs(cards[0][0], cards[0][1], cards[1][0], cards[1][1])
        for c in cards:
            board[c[0]][c[1]] = 0
        f(cards[1][0], cards[1][1], per, index+1, dist+d)
        for c in cards:
            board[c[0]][c[1]] = per[index]

        d = bfs(x, y, cards[1][0], cards[1][1]) + bfs(cards[1][0], cards[1][1], cards[0][0], cards[0][1])
        for c in cards:
            board[c[0]][c[1]] = 0
        f(cards[0][0], cards[0][1], per, index+1, dist+d)
        for c in cards:
            board[c[0]][c[1]] = per[index]

    pos = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0: pos[board[i][j]].append((i, j))

    orders = list(permutations(pos.keys(), len(pos.keys())))
    ans = []
    for order in orders:
        f(r, c, order, 0, 0)

    return min(ans) + len(pos) * 2


'''
# 56.7 / 100
# 실패 + 시간초과
def solution(board, r, c):
    from collections import defaultdict
    from itertools import permutations
    def bfs(x, y, a, b):
        queue = [(x, y)]
        ret = 0
        visited = [[0 for _ in range(4)] for _ in range(4)]
        while queue:
            if (a, b) in queue: return ret
            ret += 1
            next = set()
            for q in queue:
                if q[0]+1 in range(0, 4) and visited[q[0]+1][q[1]] == 0:
                    next.add((q[0]+1, q[1]))
                    visited[q[0]+1][q[1]] = 1
                if q[0]-1 in range(0, 4) and visited[q[0]-1][q[1]] == 0:
                    next.add((q[0]-1, q[1]))
                    visited[q[0]-1][q[1]] = 1
                if q[1]+1 in range(0, 4) and visited[q[0]][q[1]+1] == 0:
                    next.add((q[0], q[1]+1))
                    visited[q[0]][q[1]+1] = 1
                if q[1]-1 in range(0, 4) and visited[q[0]][q[1]-1] == 0:
                    next.add((q[0], q[1]-1))
                    visited[q[0]][q[1]-1] = 1
                for i in range(1, 4):
                    if q[0]+i == 3: next.add((q[0]+i, q[1]))
                    elif q[0]+i in range(0, 4) and _board[q[0]+i][q[1]] + visited[q[0]+i][q[1]] != 0:
                        next.add((q[0]+i, q[1]))
                        visited[q[0]+i][q[1]] = 1
                    if q[0]-i == 0: next.add((q[0]-i, q[1]))
                    elif q[0]-i in range(0, 4) and _board[q[0]-i][q[1]] + visited[q[0]-i][q[1]] != 0:
                        next.add((q[0]-i, q[1]))
                        visited[q[0]-i][q[1]] = 1
                    if q[1]+i == 3: next.add((q[0], q[1]+i))
                    elif q[1]+i in range(0, 4) and _board[q[0]][q[1]+i] + visited[q[0]][q[1]+i] != 0:
                        next.add((q[0], q[1]+i))
                        visited[q[0]][q[1]+i] = 1
                    if q[1]-i == 0: next.add((q[0], q[1]-i))
                    elif q[1]-i in range(0, 4) and _board[q[0]][q[1]-i] + visited[q[0]][q[1]-i] != 0:
                        next.add((q[0], q[1]-i))
                        visited[q[0]][q[1]-i] = 1
            queue = list(next)
        return -1

    pos = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0: pos[board[i][j]].append((i, j))

    orders = list(permutations(pos.keys(), len(pos.keys())))
    neworder = []
    for order in orders:
        for i in range(2**len(pos)):
            tmp = []
            for j in range(len(order)):
                if bin(i)[2:].zfill(len(pos))[j] == '0':
                    tmp.append((order[j], 0))
                else:
                    tmp.append((order[j], 1))
            neworder.append(tuple(tmp))
    # for z in neworder: print(z)

    ans = 10**6
    for order in neworder:
        cnt = 0
        x, y = r, c
        _board = [[a for a in b] for b in board]
        for o, z in order:
            cnt += bfs(x, y, pos[o][z][0], pos[o][z][1])
            cnt += bfs(pos[o][z][0], pos[o][z][1], pos[o][1-z][0], pos[o][1-z][1])
            x, y = pos[o][1-z][0], pos[o][1-z][1]
            _board[pos[o][z][0]][pos[o][z][1]] = 0
            _board[pos[o][1-z][0]][pos[o][1-z][1]] = 0
        ans = min(ans, cnt)
        # print(ans)
    return ans + len(pos) * 2
'''

'''
# 66.7 / 100
# 두 카드간 순서 미고려시
def solution(board, r, c):
    from collections import defaultdict
    from itertools import permutations
    def bfs(x, y, a, b):
        queue = [(x, y)]
        ret = 0
        while queue:
            if (a, b) in queue: return ret
            ret += 1
            next = set()
            for q in queue:
                if q[0]+1 in range(0, 4): next.add((q[0]+1, q[1]))
                if q[0]-1 in range(0, 4): next.add((q[0]-1, q[1]))
                if q[1]+1 in range(0, 4): next.add((q[0], q[1]+1))
                if q[1]-1 in range(0, 4): next.add((q[0], q[1]-1))
                for i in range(1, 4):
                    if q[0]+i == 3: next.add((q[0]+i, q[1]))
                    elif q[0]+i in range(0, 4) and _board[q[0]+i][q[1]] != 0:
                        next.add((q[0]+i, q[1]))
                    if q[0]-i == 0: next.add((q[0]-i, q[1]))
                    elif q[0]-i in range(0, 4) and _board[q[0]-i][q[1]] != 0:
                        next.add((q[0]-i, q[1]))
                    if q[1]+i == 3: next.add((q[0], q[1]+i))
                    elif q[1]+i in range(0, 4) and _board[q[0]][q[1]+i] != 0:
                        next.add((q[0], q[1]+i))
                    if q[1]-i == 0: next.add((q[0], q[1]-i))
                    elif q[1]-i in range(0, 4) and _board[q[0]][q[1]-i] != 0:
                        next.add((q[0], q[1]-i))
            queue = list(next)
        return -1

    pos = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0: pos[board[i][j]].append((i, j))

    orders = list(permutations(pos.keys(), len(pos.keys())))
    ans = 10**6
    for order in orders:
        cnt = 0
        x, y = r, c
        _board = [[a for a in b] for b in board]
        for o in order:
            dist1 = bfs(x, y, pos[o][0][0], pos[o][0][1])
            dist2 = bfs(x, y, pos[o][1][0], pos[o][1][1])

            if dist1 < dist2:
                cnt += dist1 + bfs(pos[o][0][0], pos[o][0][1], pos[o][1][0], pos[o][1][1])
                x, y = pos[o][1][0], pos[o][1][1]
            else:
                cnt += dist2 + bfs(pos[o][1][0], pos[o][1][1], pos[o][0][0], pos[o][0][1])
                x, y = pos[o][0][0], pos[o][0][1]
            _board[pos[o][0][0]][pos[o][0][1]] = 0
            _board[pos[o][1][0]][pos[o][1][1]] = 0
        ans = min(ans, cnt)
        # print(ans)
    return ans + len(pos) * 2
'''

# a = [[1,0,0,3],
#      [2,0,0,0],
#      [0,0,0,2],
#      [3,0,1,0]]
# a = [[0,0,0,0],
#      [2,0,0,0],
#      [0,0,0,2],
#      [0,0,0,0]]
a = [[1, 5, 0, 2], [6, 4, 3, 0], [0, 2, 1, 5], [3, 0, 6, 4]]
b = 0
c = 0

if __name__=='__main__':
    print(solution(a, b, c))