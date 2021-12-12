def solution(numbers, hand):
    pos = {1: (0, 0), 2: (0, 1), 3: (0, 2),
           4: (1, 0), 5: (1, 1), 6: (1, 2),
           7: (2, 0), 8: (2, 1), 9: (2, 2),
                      0: (3, 1)}

    l, r = (3, 0), (3, 2)
    ans = []
    for n in numbers:
        dist_l = abs(pos[n][0] - l[0]) + abs(pos[n][1] - l[1])
        dist_r = abs(pos[n][0] - r[0]) + abs(pos[n][1] - r[1])

        if n in (1, 4, 7):
            ans.append('L')
            l = pos[n]
        elif n in (3, 6, 9):
            ans.append('R')
            r = pos[n]
        elif dist_l < dist_r:
            ans.append('L')
            l = pos[n]
        elif dist_r < dist_l:
            ans.append('R')
            r = pos[n]
        elif hand == 'left':
            ans.append('L')
            l = pos[n]
        elif hand == 'right':
            ans.append('R')
            r = pos[n]
    
    return ''.join(ans)

a = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
b = "right"

if __name__=='__main__':
    print(solution(a, b))