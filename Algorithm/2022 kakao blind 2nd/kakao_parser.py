############################################################
### kakao_parser.py
# REST api parser for communicate with server
# ============================================
# api_start(base_url, x_auth_token, problem)
# api_waiting_line(base_url, auth_key)
# api_game_result(base_url, auth_key)
# api_user_info(base_url, auth_key)
# api_match(base_url, auth_key, pairs)
# api_change_grade(base_url, auth_key, commands)
# api_score(base_url, auth_key)

# REST api
import requests
import json

# debug
import sys

############################################################
# Response Code	            | Description
# __________________________________________________________
# 200 OK	                | 성공
# 400 Bad Request	        | Parameter가 잘못됨 (범위, 값 등)
# 401 Unauthorized	        | 인증을 위한 Header가 잘못됨
# 500 Internal Server Error	| 서버 에러, 채팅으로 문의 요망

# Constants
WRONG_STATUS_CODE = (400, 401, 500)

### Start API
# params :  problem - int, problem number
# return :  auth
def api_start(base_url, x_auth_token, problem):
    headers = {'X-Auth-Token': x_auth_token, 'Content-Type': 'application/json'}
    data = {'problem': problem}
    r = requests.post(base_url + '/start', headers=headers, data=json.dumps(data))

    if r.status_code in WRONG_STATUS_CODE:
        print(f"RESPONSE {r.status_code} IN {sys._getframe(0).f_code.co_name}")
        print(r.content)
        sys.exit()

    json_r = json.loads(r.content)
    return json_r['auth_key']

### WaitingLine API
# params :  auth_key - str, auth_key of problem
# return :  waiting_line - json dict (id, from)
def api_waiting_line(base_url, auth_key):
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    r = requests.get(base_url + '/waiting_line', headers=headers)

    if r.status_code in WRONG_STATUS_CODE:
        print(f"RESPONSE {r.status_code} IN {sys._getframe(0).f_code.co_name}")
        print(r.content)
        sys.exit()

    json_r = json.loads(r.content)
    return json_r['waiting_line']

### GameResult API
# params :  auth_key - str, auth_key of problem
# return :  game_result - json dict (win, lose, taken)
def api_game_result(base_url, auth_key):
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    r = requests.get(base_url + '/game_result', headers=headers)

    if r.status_code in WRONG_STATUS_CODE:
        print(f"RESPONSE {r.status_code} IN {sys._getframe(0).f_code.co_name}")
        print(r.content)
        sys.exit()

    json_r = json.loads(r.content)
    return json_r['game_result']

### UserInfo API
# params :  auth_key - str, auth_key of problem
# return :  user_info - json dict (id, grade)
def api_user_info(base_url, auth_key):
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    r = requests.get(base_url + '/user_info', headers=headers)

    if r.status_code in WRONG_STATUS_CODE:
        print(f"RESPONSE {r.status_code} IN {sys._getframe(0).f_code.co_name}")
        print(r.content)
        sys.exit()

    json_r = json.loads(r.content)
    return json_r['user_info']

### Match API
# params :  auth_key - str, auth_key of problem
#           pairs - list of lists, list of user matching
# return :  status - str, status of server
#           time - int, time (request time + 1)
def api_match(base_url, auth_key, pairs):
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    data = {'pairs': pairs}
    r = requests.put(base_url + '/match', headers=headers, data=json.dumps(data))

    if r.status_code in WRONG_STATUS_CODE:
        print(f"RESPONSE {r.status_code} IN {sys._getframe(0).f_code.co_name}")
        print(r.content)
        sys.exit()

    json_r = json.loads(r.content)
    return json_r['status'], int(json_r['time'])

### ChangeGrade API
# params :  auth_key - str, auth_key of problem
#           pairs - list of commands, ()
# return :  status - str, status of server
#           time - int, time (request time + 1)
def api_change_grade(base_url, auth_key, commands):
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    data = {'commands': commands}
    r = requests.put(base_url + '/change_grade', headers=headers, data=json.dumps(data))

    if r.status_code in WRONG_STATUS_CODE:
        print(f"RESPONSE {r.status_code} IN {sys._getframe(0).f_code.co_name}")
        print(r.content)
        sys.exit()

    json_r = json.loads(r.content)
    return json_r['status']

### Score API
# params :  auth_key - str, auth_key of problem
# return :  status - str, status of server (finish required)
#           efficiency_score - float
#           accuracy_score1 - float
#           accuracy_score2 - float
#           score - float
def api_score(base_url, auth_key):
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    r = requests.get(base_url + '/score', headers=headers)

    if r.status_code in WRONG_STATUS_CODE:
        print(f"RESPONSE {r.status_code} IN {sys._getframe(0).f_code.co_name}")
        print(r.content)
        sys.exit()

    json_r = json.loads(r.content)
    return json_r['status'], json_r['efficiency_score'], \
        json_r['accuracy_score1'], json_r['accuracy_score2'], json_r['score']