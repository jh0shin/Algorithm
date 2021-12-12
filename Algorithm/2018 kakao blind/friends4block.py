def solution(m, n, board):
    board = [[j for j in i] for i in board]
    while 1:
        new = [[j for j in i] for i in board]
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1] != '@':
                    new[i][j] = new[i+1][j] = new[i][j+1] = new[i+1][j+1] = '@'

        for j in range(n):
            tmp = []
            for i in range(m):
                if new[i][j] != '@':
                    tmp.append(new[i][j])
                    new[i][j] = '@'
            for i in range(len(tmp)):
                new[m-1-i][j] = tmp[-i-1]

        if new == board: break
        board = new

        # for a in new:
        #     print(a)
        # print()

    return sum([a.count('@') for a in board])
  

a = 6
b = 6
c = ["AABBEE","AAAEEE","VAAEEV","AABBEE","AACCEE","VVCCEE" ]

if __name__=='__main__':
    print(solution(a, b, c))