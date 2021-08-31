def solution(board):
    import heapq
    n = len(board)
    direction = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
    dp = [[[float('inf') for _ in range(4)] for _ in range(n)] for i in range(n)]

    q = []
    if board[1][0] != 1: heapq.heappush(q, (100, 0, 1, 0))
    if board[0][1] != 1: heapq.heappush(q, (100, 1, 0, 1))
    while q:
        cost, drct, x, y = heapq.heappop(q)
        if x not in range(n) or y not in range(n): continue
        if dp[x][y][drct] < cost: continue
        if board[x][y] == 0: dp[x][y][drct] = cost
        else: continue

        for i in range(-1, 2):
            nx, ny = direction[(drct+i)%4]
            heapq.heappush(q, (cost+600 if i%2 == 1 else cost+100, (drct+i)%4, x+nx, y+ny))
    
    return min(dp[n-1][n-1])


a = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]

if __name__=='__main__':
    print(solution(a))