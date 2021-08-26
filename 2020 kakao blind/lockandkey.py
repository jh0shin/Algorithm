'''
# 82 / 100
def solution(key, lock):
    for _ in range(4):
        for i in range(-2, len(lock)):
            for j in range(-2, len(lock)):
                tmp = [[_l for _l in l] for l in lock]
                for x in range(len(key)):
                    for y in range(len(key)):
                        if i+x in range(len(lock)) and j+y in range(len(lock)):
                            tmp[i+x][j+y] += key[x][y]

                unlock = True
                for x in tmp:
                    for y in x:
                        if y != 1: unlock = False
                
                if unlock == True:
                    return True
        
        tmp = [[_k for _k in k] for k in key]
        for i in range(len(key)):
            for j in range(len(key)):
                key[i][j] = tmp[len(key)-1-j][i]
        
    return False
'''

def solution(key, lock):
    for _ in range(4):
        for i in range(-len(key)+1, len(lock)):
            for j in range(-len(key)+1, len(lock)):
                tmp = [[_l for _l in l] for l in lock]
                for x in range(len(key)):
                    for y in range(len(key)):
                        if i+x in range(len(lock)) and j+y in range(len(lock)):
                            tmp[i+x][j+y] += key[x][y]

                unlock = True
                for x in tmp:
                    for y in x:
                        if y != 1: unlock = False
                
                if unlock == True:
                    return True
        
        tmp = [[_k for _k in k] for k in key]
        for i in range(len(key)):
            for j in range(len(key)):
                key[i][j] = tmp[len(key)-1-j][i]
        
    return False

a = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
b = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

if __name__=='__main__':
    print(solution(a, b))