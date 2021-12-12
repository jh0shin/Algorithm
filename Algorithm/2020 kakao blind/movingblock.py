def solution(board):
    N = len(board)
    visited = {(0, 0, 0)}
    ans = 1
    cur = [(0, 0, 0)]
    while cur != []:
        next = []
        for x, y, s in cur: # s : 0(가로), 1(세로)
            if x > 0 and board[x-1][y] + board[x-1+s][y+1-s] == 0:
                if (x-1, y, s) not in visited:
                    visited.add((x-1, y, s))
                    next.append((x-1, y, s))
            if x+s < N-1 and board[x+1][y] + board[x+1+s][y+1-s] == 0:
                if (x+1, y, s) not in visited:
                    visited.add((x+1, y, s))
                    next.append((x+1, y, s))
            if y > 0 and board[x][y-1] + board[x+s][y-s] == 0:
                if (x, y-1, s) not in visited:
                    visited.add((x, y-1, s))
                    next.append((x, y-1, s))
            if y+1-s < N-1 and board[x][y+1] + board[x+s][y+2-s] == 0:
                if (x, y+1, s) not in visited:
                    visited.add((x, y+1, s))
                    next.append((x, y+1, s))

            if s == 0:
                if x > 0 and board[x-1][y] + board[x-1][y+1] == 0:
                    if (x-1, y, 1) not in visited:
                        visited.add((x-1, y, 1))
                        next.append((x-1, y, 1))
                    if (x-1, y+1, 1) not in visited:
                        visited.add((x-1, y+1, 1))
                        next.append((x-1, y+1, 1))
                if x < N-1 and board[x+1][y] + board[x+1][y+1] == 0:
                    if (x, y, 1) not in visited:
                        visited.add((x, y, 1))
                        next.append((x, y, 1))
                    if (x, y+1, 1) not in visited:
                        visited.add((x, y+1, 1))
                        next.append((x, y+1, 1))

            if s == 1:
                if y > 0 and board[x][y-1] + board[x+1][y-1] == 0:
                    if (x, y-1, 0) not in visited:
                        visited.add((x, y-1, 0))
                        next.append((x, y-1, 0))
                    if (x+1, y-1, 0) not in visited:
                        visited.add((x+1, y-1, 0))
                        next.append((x+1, y-1, 0))
                if y < N-1 and board[x][y+1] + board[x+1][y+1] == 0:
                    if (x, y, 0) not in visited:
                        visited.add((x, y, 0))
                        next.append((x, y, 0))
                    if (x+1, y, 0) not in visited:
                        visited.add((x+1, y, 0))
                        next.append((x+1, y, 0))

        # print(ans, next)
        if (N-1, N-2, 0) in next or (N-2, N-1, 1) in next:
            break
        
        ans += 1
        cur = next
    
    return ans


a = [[0, 0, 0, 1, 1],
     [0, 0, 0, 1, 0],
     [0, 1, 0, 1, 1],
     [1, 1, 0, 0, 1],
     [0, 0, 0, 0, 0]]

if __name__=='__main__':
    print(solution(a))