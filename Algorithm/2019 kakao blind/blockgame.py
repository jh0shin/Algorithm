def solution(board):
    ans = 0
    N = len(board)

    while 1:
        isdeleted = False

        for j in range(N):
            for i in range(N):
                if board[i][j] > 0: break
                else: board[i][j] = -1

        for i in range(N-1):
            for j in range(N-2):
                tmp = []
                for x in range(2):
                    for y in range(3):
                        tmp.append(board[i+x][j+y])
                tset = set(tmp) - {-1}
                if tset != {0} and len(tset) == 1 and tmp.count(list(tset)[0]) == 4:
                    # print(i, j)
                    for x in range(2):
                        for y in range(3):
                            board[i+x][j+y] = 0
                    ans += 1
                    isdeleted = True
                
        for i in range(N-2):
            for j in range(N-1):
                tmp = []
                for x in range(3):
                    for y in range(2):
                        tmp.append(board[i+x][j+y])
                tset = set(tmp) - {-1}
                if tset != {0} and len(tset) == 1 and tmp.count(list(tset)[0]) == 4:
                    # print(i, j)
                    for x in range(3):
                        for y in range(2):
                            board[i+x][j+y] = 0
                    ans += 1
                    isdeleted = True

        if isdeleted == False: break

    return ans

a = [[0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,4,0,0,0],
     [0,0,0,0,0,4,4,0,0,0],
     [0,0,0,0,3,0,4,0,0,0],
     [0,0,0,2,3,0,0,0,5,5],
     [1,2,2,2,3,3,0,0,0,5],
     [1,1,1,0,0,0,0,0,0,5]
    ]

if __name__=='__main__':
    print(solution(a))