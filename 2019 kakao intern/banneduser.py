def solution(user_id, banned_id):
    from functools import reduce
    from math import factorial
    import re
    userv = [0 for _ in range(len(user_id))]
    cnt = {k: banned_id.count(k) for k in banned_id}
    s = set()
    # print(cnt)
    
    def dfs(i):
        if i == len(banned_id):
            s.add(''.join(list(map(str, userv))))
            return
        for j in range(len(user_id)):
            if userv[j] == 1: continue
            # print(banned_id[i].replace('*', '.'), user_id[j])
            if len(banned_id[i]) != len(user_id[j]): continue
            elif re.match(banned_id[i].replace('*', '.'), user_id[j]):
                userv[j] = 1
                dfs(i+1)
                # print(tmpsum, i+1, userv)
                userv[j] = 0
    
    dfs(0)
    return len(s)

a = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
b = ["*rodo", "*rodo", "******"]

if __name__=='__main__':
    print(solution(a, b))