def solution(food_times, k):
    l, r = 1, 100000000
    while l < r:
        mid = (l+r)//2
        tmp_sum = sum([min(f, mid) for f in food_times])
        # print(l, r, mid, tmp_sum)
        if tmp_sum <= k:
            l = mid + 1
        else:
            r = mid
    
    tmp = [i for i in range(len(food_times)) if food_times[i] >= l]
    # print(tmp)

    if len(tmp) == 0: return -1
    else: return tmp[k-tmp_sum] + 1
    
a = [3, 1, 2]
b = 5

if __name__=='__main__':
    print(solution(a, b))