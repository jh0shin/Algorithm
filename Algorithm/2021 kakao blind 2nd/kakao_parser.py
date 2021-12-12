############################################################
### kakao_parser.py
# REST api parser for communicate with server
# ============================================
# api_start(base_url, x_auth_token, problem)
# api_locations(base_url, auth_key)
# api_trucks(base_url, auth_key)
# api_simulate(base_url, auth_key, commands)
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

### Locations API
# params :  auth_key - str, auth_key of problem
# return :  locations - json dict
def api_locations(base_url, auth_key):
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    r = requests.get(base_url + '/locations', headers=headers)

    if r.status_code in WRONG_STATUS_CODE:
        print(f"RESPONSE {r.status_code} IN {sys._getframe(0).f_code.co_name}")
        print(r.content)
        sys.exit()

    json_r = json.loads(r.content)
    return json_r['locations']

### Trucks API
# params :  auth_key - str, auth_key of problem
# return :  trucks - json dict
def api_trucks(base_url, auth_key):
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    r = requests.get(base_url + '/trucks', headers=headers)

    if r.status_code in WRONG_STATUS_CODE:
        print(f"RESPONSE {r.status_code} IN {sys._getframe(0).f_code.co_name}")
        print(r.content)
        sys.exit()

    json_r = json.loads(r.content)
    return json_r['trucks']

### Simulate API
# params :  auth_key - str, auth_key of problem
#           commands - list of dicts, list of commands
# return :  status - str, status of server
#           time - int, time (request time + 1)
#           failed_requests_count - int
#           distance - str, sum of truck 
def api_simulate(base_url, auth_key, commands):
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    data = {'commands': commands}
    r = requests.put(base_url + '/simulate', headers=headers, data=json.dumps(data))

    if r.status_code in WRONG_STATUS_CODE:
        print(f"RESPONSE {r.status_code} IN {sys._getframe(0).f_code.co_name}")
        print(r.content)
        sys.exit()

    json_r = json.loads(r.content)
    return json_r['status'], int(json_r['time']), \
        int(float(json_r['failed_requests_count'])), float(json_r['distance'])

### Score API
# params :  auth_key - str, auth_key of problem
# return :  score - float
def api_score(base_url, auth_key):
    headers = {'Authorization': auth_key, 'Content-Type': 'application/json'}
    r = requests.get(base_url + '/score', headers=headers)

    if r.status_code in WRONG_STATUS_CODE:
        print(f"RESPONSE {r.status_code} IN {sys._getframe(0).f_code.co_name}")
        print(r.content)
        sys.exit()

    json_r = json.loads(r.content)
    return json_r['score']