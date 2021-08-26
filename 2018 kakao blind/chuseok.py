def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        tmp = arr1[i] | arr2[i]
        ans.append(bin(tmp)[2:].zfill(n).replace('0', ' ').replace('1', '#'))
    return ans

a = 6
b = [46, 33, 33 ,22, 31, 50]
c = [27 ,56, 19, 14, 14, 10]

if __name__=='__main__':
    print(solution(a, b, c))