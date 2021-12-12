def solution(n, s, a, b, fares):
    s, a, b = s-1, a-1, b-1
    fw = [[10**21 for _ in range(n)] for _ in range(n)]
    for i in range(n): fw[i][i] = 0
    for f, r, v in fares:
        fw[f-1][r-1] = fw[r-1][f-1] = v
    for k in range(n):
        for i in range(n):
            for j in range(n):
                fw[i][j] = min(fw[i][j], fw[i][k]+fw[k][j])
    ans = fw[s][a] + fw[s][b]
    for via in range(n):
        ans = min(ans, fw[s][via]+fw[via][a]+fw[via][b])

    return ans

a = 6
b = 4
c = 5
d = 6
e = [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]

if __name__=='__main__':
    print(solution(a, b, c, d, e))