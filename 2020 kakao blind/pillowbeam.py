def solution(n, build_frame):
    def f(_pillow, _beam):
        cp = [_ for _ in _pillow]
        cb = [_ for _ in _beam]

        for x, y in _pillow:
            if y == 0: cp.remove((x, y))
            if (x, y+1) in cp: cp.remove((x, y+1))
            if (x-1, y+1) in cb: cb.remove((x-1, y+1))
            if (x, y+1) in cb: cb.remove((x, y+1))
        
        for x, y in _beam:
            if (x-1, y) in _beam and (x+1, y) in _beam and (x, y) in cb: cb.remove((x, y))
            if (x, y) in cp: cp.remove((x, y))
            if (x+1, y) in cp: cp.remove((x+1, y))            
        
        if cp == [] and cb == []: return True
        else: return False

    pillow = []
    beam = []

    for x, y, a, b in build_frame:
        if a == 0 and b == 1:
            if (x, y) not in pillow and f(pillow+[(x, y)], beam):
                pillow.append((x, y))
        elif a == 0 and b == 0:
            _pillow = [_ for _ in pillow]
            _pillow.remove((x, y))
            if (x, y) in pillow and f(_pillow, beam):
                pillow.remove((x, y))
        elif a == 1 and b == 1:
            if (x, y) not in beam and f(pillow, beam+[(x, y)]):
                beam.append((x, y))
        elif a == 1 and b == 0:
            _beam = [_ for _ in beam]
            _beam.remove((x, y))
            if (x, y) in beam and f(pillow, _beam):
                beam.remove((x, y))
    
    ans = []
    for p in pillow: ans.append([p[0], p[1], 0])
    for b in beam: ans.append([b[0], b[1], 1])
    ans.sort()

    return ans


a = 5
b = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

if __name__=='__main__':
    print(solution(a, b))