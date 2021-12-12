def solution(record):
    from collections import deque
    user = {}
    log = deque()
    for r in record:
        if r.startswith("Enter"):
            _, id, name = r.split()
            user[id] = name
            log.append((id, 0))
        elif r.startswith("Leave"):
            _, id = r.split()
            # user.pop(id)
            log.append((id, 1))
        elif r.startswith("Change"):
            _, id, name = r.split()
            user[id] = name
    
    ans = []
    while log:
        if log[0][1] == 0:
            ans.append(f"{user[log[0][0]]}님이 들어왔습니다.")
        elif log[0][1] == 1:
            ans.append(f"{user[log[0][0]]}님이 나갔습니다.")
        log.popleft()
    
    return ans

a = ["Enter uid1234 Muzi",
     "Enter uid4567 Prodo",
     "Leave uid1234",
     "Enter uid1234 Prodo",
     "Change uid4567 Ryan"
    ]

if __name__=='__main__':
    print(solution(a))