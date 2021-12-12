def solution(stones, k):
    l, r = 1, max(stones)+1

    while l < r:
        mid = (l+r)//2
        tmp, cnt = 0, 1
        for stone in stones:
            if stone < mid:
                tmp += 1
                # print('X', end='')
            else:
                cnt = max(cnt, tmp+1)
                tmp = 0
                # print(stone, end='')
        cnt = max(cnt, tmp+1)
        # print(' : ', l, r, mid, cnt)
        if cnt > k:
            r = mid
        else:
            l = mid+1
    
    return l-1

# a = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
# b = 3

a = [2]
b = 1

if __name__=='__main__':
    print(solution(a, b))