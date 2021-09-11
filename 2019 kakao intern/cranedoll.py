def solution(board, moves):
    from collections import deque  
    bucket = deque([])
    ans = 0
    for move in moves:
        for row in range(len(board)):
            if board[row][move-1] == 0: continue

            bucket.append(board[row][move-1])
            board[row][move-1] = 0

            if len(bucket) > 1 and bucket[-1] == bucket[-2]:
                ans += 2
                bucket.pop()
                bucket.pop()
            break
    
    return ans

a = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
b = [1,5,3,5,1,2,1,4]

if __name__=='__main__':
    print(solution(a, b))