def solution(n, k, cmd):
    from collections import deque, defaultdict
    sheet = defaultdict(list)
    undo = deque()

    for i in range(n-1): sheet[i] = [i-1, i+1]
    sheet[n-1] = [n-2, -1]

    for c in cmd:
        if c == 'C':
            undo.append((k, sheet[k]))
            if sheet[k][1] == -1:
                k = sheet[k][0]
                sheet[k][1] = -1
            elif sheet[k][0] == -1:
                k = sheet[k][1]
                sheet[k][0] = -1
            else:
                sheet[sheet[k][0]][1] = sheet[k][1]
                sheet[sheet[k][1]][0] = sheet[k][0]
                k = sheet[k][1]
            sheet.pop(undo[-1][0])
        elif c == 'Z':
            u = undo.pop()
            if u[1][0] != -1: sheet[u[1][0]][1] = u[0]
            if u[1][1] != -1: sheet[u[1][1]][0] = u[0]
            sheet[u[0]] = u[1]
        elif c[0] == 'U':
            x = int(c.split()[1])
            for _ in range(x): k = sheet[k][0]
        elif c[0] == 'D':
            x = int(c.split()[1])
            for _ in range(x): k = sheet[k][1]
        # print(k, sheet, undo)
    
    return ''.join(['O' if i in sheet.keys() else 'X' for i in range(n)])

a = 8
b = 2
c = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

if __name__=='__main__':
    print(solution(a, b, c))