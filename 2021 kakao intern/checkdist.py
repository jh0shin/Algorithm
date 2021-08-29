def solution(places):
    la = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    lb = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    def f(place):
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P':
                    for a, b in la:
                        if x+a in range(5) and y+b in range(5) and place[x+a][y+b] =='P':
                            return 0
                        if x+a*2 in range(5) and y+b*2 in range(5) and place[x+a*2][y+b*2] == 'P':
                            if place[x+a][y+b] == 'O': return 0
                    for a, b in lb:
                        if x+a in range(5) and y+b in range(5) and place[x+a][y+b] =='P':
                            if place[x+a][y] == 'O' or place[x][y+b] == 'O': return 0  
        return 1

    return [f(place) for place in places] 

a = [["POOOP",
      "OXXOX",
      "OPXPX",
      "OOXOX",
      "POXXP"],
     ["POOPX",
      "OXPXP",
      "PXXXO",
      "OXXXO",
      "OOOPP"],
     ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
     ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
     ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

if __name__=='__main__':
    print(solution(a))