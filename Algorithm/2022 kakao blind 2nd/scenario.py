############################################################
### scenario.py
# Scenarios for each problem
# format : [{"truck_id": 0, "command": [2, 5, 4, 1, 6]}, ... ]
# ==========================================================
# scenario_1(base_url, x_auth_token)
# scenario_2(base_url, x_auth_token)

from kakao_parser import *
from strategy import *

from collections import defaultdict

############################################################
### Scenario 1
def scenario_1(base_url, x_auth_token):
    ### Get auth_key
    pkey = api_start(base_url, x_auth_token, 1)

    ### Before start matching, set every user's grade to 5000
    init_commands = []
    for i in range(30):
        init_commands.append({'id': i+1, 'grade': 5000})
    server_status = api_change_grade(base_url, pkey, init_commands)
    if server_status != 'ready':
        print(f"InitGradeError")
        return    

    ### DEBUG
    # print(init_commands)

    server_time = 0
    while 1:
        ### Get waiting queue information and user information
        waiting_line = api_waiting_line(base_url, pkey)
        user_info = api_user_info(base_url, pkey)

        ### User infomation parsing        
        parsed_user_info = {}
        for user in user_info:
            parsed_user_info[user['id']] = user['grade']

        ### Get next matching pairs according to matching strategy
        # matching_pairs = match_FIFO(waiting_line, parsed_user_info)
        # matching_pairs = match_score(waiting_line, parsed_user_info)
        matching_pairs = match_score2(waiting_line, parsed_user_info, 120)
        # matching_pairs = match_score_time(waiting_line, parsed_user_info, 100, 13)
        
        ### Send next matching info
        server_status, server_time = api_match(base_url, pkey, matching_pairs)
        if server_status not in ('ready', 'finished'):
            print(f"MatchError at servertime {server_time}")
            return

        ### Break if server is finished
        if server_status == 'finished':
            break

        ### Get game result
        game_result = api_game_result(base_url, pkey)

        ### Adjust user score
        commands = score_const(game_result, parsed_user_info)
        # commands = score_const2(game_result, parsed_user_info, 55)
        # commands = score_time(game_result, parsed_user_info, server_time)
        # commands = score_const3(game_result, parsed_user_info)

        server_status = api_change_grade(base_url, pkey, commands)
        if server_status != 'ready':
            print(f"ChangeGradeError at servertime {server_time}")
            return

        ### Server time log
        if server_time % 60 == 0:
            print(f"SERVER TIME : {server_time}")
        
        ### DEBUG
        # print(f"SERVER TIME : {server_time}")
        # print("WAITING LINE AND USER INFO")
        # print(waiting_line)
        # print(user_info)
        # print("MATCHING PAIRS")
        # print(matching_pairs)
        # print("GAME RESULT")
        # print(game_result)
        # print("COMMANDS")
        # print(commands)

    ### DEBUG
    # Score list
    print(sorted([user['grade'] for user in user_info]))

    score = api_score(base_url, pkey)
    print(f"Scenario 1 score : {score}")    

############################################################
### Problem 2
def scenario_2(base_url, x_auth_token):
    ### Get auth_key
    pkey = api_start(base_url, x_auth_token, 2)

    ### Abusing check
    game_log = defaultdict(lambda: [[], [], []]) # win, lose, lose in 3 ~ 10 min

    ### Before start matching, set every user's grade to 5000
    init_commands = []
    for i in range(900):
        init_commands.append({'id': i+1, 'grade': 5000})
    server_status = api_change_grade(base_url, pkey, init_commands)
    if server_status != 'ready':
        print(f"InitGradeError")
        return    

    ### DEBUG
    # print(init_commands)

    server_time = 0
    while 1:
        ### Get waiting queue information and user information
        waiting_line = api_waiting_line(base_url, pkey)
        user_info = api_user_info(base_url, pkey)

        ### Waiting list and user infomation parsing
        waiting_list = []
        for user in waiting_line:
            waiting_list.append((user['from'], user['id']))
        waiting_list.sort()
        
        parsed_user_info = {}
        for user in user_info:
            parsed_user_info[user['id']] = user['grade']

        ### Get next matching pairs according to matching strategy
        # matching_pairs = match_FIFO(waiting_line, parsed_user_info)
        # matching_pairs = match_score(waiting_line, parsed_user_info)
        # matching_pairs = match_score2(waiting_line, parsed_user_info, 200)
        # matching_pairs = match_score_time(waiting_line, parsed_user_info, 100, 10)
        # matching_pairs = match_rate(waiting_line, parsed_user_info, game_log)
        # matching_pairs = match_rate2(waiting_line, parsed_user_info, game_log)
        # matching_pairs = match_rate3(waiting_line, parsed_user_info, game_log)
        # matching_pairs = match_rate4(waiting_line, parsed_user_info, game_log)
        matching_pairs = match_rate5(waiting_line, parsed_user_info, game_log)
        
        ### Send next matching info
        server_status, server_time = api_match(base_url, pkey, matching_pairs)
        if server_status not in ('ready', 'finished'):
            print(f"MatchError at servertime {server_time}")
            return

        ### Break if server is finished
        if server_status == 'finished':
            break

        ### Get game result
        game_result = api_game_result(base_url, pkey)
        for game in game_result:
            game_log[game['win']][0].append((game['taken'], game['lose']))
            if game['taken'] in (3, 11):
                game_log[game['lose']][2].append((game['taken'], game['win']))
            else:
                game_log[game['lose']][1].append((game['taken'], game['win']))

        ### Adjust user score
        commands = score_const(game_result, parsed_user_info)
        # commands = score_const2(game_result, parsed_user_info, 45)
        # commands = score_time(game_result, parsed_user_info, server_time)
        # commands = score2_const(game_result, parsed_user_info)
        # commands = score2_const2(game_result, parsed_user_info)

        server_status = api_change_grade(base_url, pkey, commands)
        if server_status != 'ready':
            print(f"ChangeGradeError at servertime {server_time}")
            return
        
        ### Server time log
        if server_time % 60 == 0:
            print(f"SERVER TIME : {server_time}")
        
        ### DEBUG
        # print(f"SERVER TIME : {server_time}")
        # print("WAITING LINE AND USER INFO")
        # print(waiting_line)
        # print(user_info)
        # print("MATCHING PAIRS")
        # print(matching_pairs)
        # print("GAME RESULT")
        # print(game_result)
        # print("COMMANDS")
        # print(commands)

    ### Abuser


    ### DEBUG
    # Score list
    print(sorted([user['grade'] for user in user_info]))

    score = api_score(base_url, pkey)
    print(f"Scenario 2 score : {score}") 