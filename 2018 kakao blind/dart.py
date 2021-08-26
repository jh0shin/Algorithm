def solution(dartResult):
    cur = 0
    score = [0, 0, 0]
    for d in dartResult:
        if d.isdigit():
            score[cur] = int(str(score[cur]) + d)
        elif d in ' SDT':
            score[cur] **= ' SDT'.index(d)
            cur += 1
        elif d == '*':
            score[cur-1] *= 2
            if cur > 1: score[cur-2] *= 2
        elif d == '#':
            score[cur-1] *= -1
    
    return sum(score)

a = '1S2D*3T'

if __name__=='__main__':
    print(solution(a))