# 오답 (46.4 / 100)
# def solution(relation):
#     from itertools import combinations
#     col = [i for i in range(len(relation[0]))]
#     ans = 0
#     for i in range(1, len(relation[0])+1):
#         if len(col) == 0: break
#         if len(col) < i: break
#         combination = list(combinations(col, i))
#         for com in combination:
#             tmp = [tuple([r[c] for c in com]) for r in relation]  
#             # print(tmp)      
#             if len(tmp) == len(set(tmp)) and sum([0 if c in col else 1 for c in com]) == 0:
#                 # print(com)
#                 ans += 1
#                 for c in com: col.remove(c)

#     return ans

def solution(relation):
    from itertools import combinations
    col = [i for i in range(len(relation[0]))]
    candidate = []
    ans = 0
    for i in range(1, len(relation[0])+1):
        if len(col) == 0: break
        if len(col) < i: break
        combination = list(combinations(col, i))
        for com in combination:
            tmp = [tuple([r[c] for c in com]) for r in relation]      
            if len(tmp) == len(set(tmp)) and sum([1 if set(cand).issubset(set(com)) else 0 for cand in candidate]) == 0:
                ans += 1
                candidate.append(com)

    return ans

a = [["100","ryan","music","2"],
     ["200","apeach","math","2"],
     ["300","tube","computer","3"],
     ["400","con","computer","4"],
     ["500","muzi","music","3"],
     ["600","apeach","music","2"]
    ]

if __name__=='__main__':
    print(solution(a))