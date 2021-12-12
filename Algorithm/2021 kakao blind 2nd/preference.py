############################################################
### perference.py
# For finding hotplace in scenario 2
# ============================================
# preference_1()

import json

############################################################
### Scenario 2
def preference_1():
    _borrow = [[0 for _ in range(60)] for _ in range(60)]
    _return = [[0 for _ in range(60)] for _ in range(60)]
    s1 = open("scenario_2/1.txt", 'r')
    data = json.loads(s1.readline())
    for k in data.keys():
        for req in data[k]:
            if int(k) in range(0, 240):
                bid = int(req[0])
                rid = int(req[1])
                # print(bid, rid)
                _borrow[bid//60][bid%60] += 1
                _return[rid//60][rid%60] += 1
    s1.close()

    for b in _borrow: print(b)
    for r in _return: print(r)