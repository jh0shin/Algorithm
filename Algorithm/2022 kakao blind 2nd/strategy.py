############################################################
### strategy.py
# Strategies for matching users efficiently and correctly

from collections import deque

############################################################
### Scenario 1 - Matching (Abuser not considered)
# FIFO
# Match user as soon as possible
# High for efficiency, not good at accuracy
def match_FIFO(waiting_line, user_info):
    # result of strategy
    pairs = []

    for t in range(len(waiting_line) // 2):
        pairs.append([waiting_line[2*t]['id'], waiting_line[2*t+1]['id']])

    return pairs

# Score
# Match user as soon as possible
# Match user with similar score
def match_score(waiting_line, user_info):
    # result of strategy
    pairs = []

    # get user score
    waiting_list = []
    for user in waiting_line:
        waiting_list.append((user_info[user['id']], user['id']))
    waiting_list.sort()

    for t in range(len(waiting_list) // 2):
        pairs.append([waiting_list[2*t][1], waiting_list[2*t+1][1]])

    return pairs

# Score2
# Match user with similar score
# if (score_diff) < score_threshold, immediately match
def match_score2(waiting_line, user_info, SCORE_TH):
    # result of strategy
    pairs = []

    # get user score
    waiting_list = []
    for user in waiting_line:
        waiting_list.append((user_info[user['id']], user['id']))
    waiting_list.sort()
    waiting_q = deque(waiting_list)

    tmp = deque([])
    while waiting_q:
        tmp.append(waiting_q.popleft())
        if len(tmp) == 2:
            if abs(tmp[0][0]-tmp[1][0]) <= SCORE_TH:
                pairs.append([tmp[0][1], tmp[1][1]])
                tmp.clear()
            else:
                tmp.popleft()

    return pairs

# Score_time
# Match user with similar score
# if (score_diff) < score_threshold, immediately match
# else match if (waiting_time) > time_threshold
def match_score_time(waiting_line, user_info, SCORE_TH, TIME_TH):
    # result of strategy
    pairs = []

    # get user score
    waiting_list = []
    for user in waiting_line:
        waiting_list.append((-user['from'], user_info[user['id']], user['id']))
    waiting_list.sort()
    waiting_q = deque(waiting_list)

    tmp = deque([])
    while waiting_q:
        tmp.append(waiting_q.pop())
        if len(tmp) == 2:
            if tmp[0][0] <= -TIME_TH or tmp[1][0] <= -TIME_TH:
                pairs.append([tmp[0][2], tmp[1][2]])
                tmp.clear()
            elif abs(tmp[0][1]-tmp[1][1]) <= SCORE_TH:
                pairs.append([tmp[0][2], tmp[1][2]])
                tmp.clear()
            else:
                tmp.popleft()

    return pairs

############################################################
### Scenario 1 - Scoring (Abuser not considered)
# Adjust constant score
# Longer the time means smaller the real score difference
# Scoring : |50 - (taken time)|
def score_const(game_result, user_info):
    # result of score adjusting
    commands = []

    # game result parsing
    for game in game_result:
        winner, loser, taken_time = game['win'], game['lose'], game['taken']
        diff = (50 - taken_time)

        win_command = {}
        win_command['id'] = winner
        win_command['grade'] = min(9999, user_info[winner] + diff)
        lose_command = {}
        lose_command['id'] = loser
        lose_command['grade'] = max(0, user_info[loser] - diff)

        commands.append(win_command)
        commands.append(lose_command)

    return commands

# Adjust constant score by parameter
# Longer the time means smaller the real score difference
# Scoring : |(CONST_TIME) - (taken time)|
def score_const2(game_result, user_info, CONST_TIME):
    # result of score adjusting
    commands = []

    # game result parsing
    for game in game_result:
        winner, loser, taken_time = game['win'], game['lose'], game['taken']
        diff = (CONST_TIME - taken_time)

        win_command = {}
        win_command['id'] = winner
        win_command['grade'] = min(9999, user_info[winner] + diff)
        lose_command = {}
        lose_command['id'] = loser
        lose_command['grade'] = max(0, user_info[loser] - diff)

        commands.append(win_command)
        commands.append(lose_command)

    return commands

# Adjust constant score
# Longer the time means smaller the real score difference
# Use power to adjust fastly
# Scoring : int((|50 - (taken time)| / 5) ** 2)
def score_const3(game_result, user_info):
    # result of score adjusting
    commands = []

    # game result parsing
    for game in game_result:
        winner, loser, taken_time = game['win'], game['lose'], game['taken']
        diff = int(((50 - taken_time) / 5) ** 2)

        win_command = {}
        win_command['id'] = winner
        win_command['grade'] = min(9999, user_info[winner] + diff)
        lose_command = {}
        lose_command['id'] = loser
        lose_command['grade'] = max(0, user_info[loser] - diff)

        commands.append(win_command)
        commands.append(lose_command)

    return commands

# Adjust constant score considering time
# Longer the time means smaller the real score difference
# User's grade will converge to original score
# So big adjusting in early games and small at the end of season
# Scoring : |50 - (taken time)| * (900 - (server time)) / 900
def score_time(game_result, user_info, server_time):
    # result of score adjusting
    commands = []

    # game result parsing
    for game in game_result:
        winner, loser, taken_time = game['win'], game['lose'], game['taken']
        diff = int((50 - taken_time) * (900 - server_time) / 900)

        win_command = {}
        win_command['id'] = winner
        win_command['grade'] = min(9999, user_info[winner] + diff)
        lose_command = {}
        lose_command['id'] = loser
        lose_command['grade'] = max(0, user_info[loser] - diff)

        commands.append(win_command)
        commands.append(lose_command)

    return commands

############################################################
### Scenario 2 - Matching (Abuser considered)
# Rate
# match user whose winrate + long loserate (over 10 min) is lower first
def match_rate(waiting_line, user_info, game_log):
    # result of strategy
    pairs = []

    # get user score
    waiting_list = []
    for user in waiting_line:
        user_id = user['id']
        if (len(game_log[user_id][0]) + len(game_log[user_id][1]) + len(game_log[user_id][2])) == 0:
            user_rate = 50
        else:
            user_rate = (len(game_log[user_id][0]) + len(game_log[user_id][1])) \
                / (len(game_log[user_id][0]) + len(game_log[user_id][1]) + len(game_log[user_id][2]))
        waiting_list.append((user_rate, user['id']))
    waiting_list.sort()

    for t in range(len(waiting_list) // 2):
        pairs.append([waiting_list[2*t][1], waiting_list[2*t+1][1]])

    return pairs

# Rate
# match users that similar user_rate
def match_rate2(waiting_line, user_info, game_log):
    # result of strategy
    pairs = []

    # get user score
    waiting_list = []
    for user in waiting_line:
        user_id = user['id']
        if (len(game_log[user_id][0]) + len(game_log[user_id][1]) + len(game_log[user_id][2])) == 0:
            user_rate = 50
        else:
            user_rate = (len(game_log[user_id][0]) + len(game_log[user_id][1])) \
                / (len(game_log[user_id][0]) + len(game_log[user_id][1]) + len(game_log[user_id][2]))
        waiting_list.append((user_info[user['id']], user_rate, user['id']))
    waiting_list.sort()
    waiting_q = deque(waiting_list)

    tmp = deque([])
    while waiting_q:
        tmp.append(waiting_q.popleft())
        if len(tmp) == 2:
            if abs(tmp[0][1]-tmp[1][1]) <= 0.2:
                pairs.append([tmp[0][2], tmp[1][2]])
                tmp.clear()
            else:
                tmp.popleft()

    return pairs

# Rate
# match user whose user_rate*user_grade is higher first
def match_rate3(waiting_line, user_info, game_log):
    # result of strategy
    pairs = []

    # get user score
    waiting_list = []
    for user in waiting_line:
        user_id = user['id']
        if (len(game_log[user_id][0]) + len(game_log[user_id][1]) + len(game_log[user_id][2])) == 0:
            user_rate = 50
        else:
            user_rate = (len(game_log[user_id][0]) + len(game_log[user_id][1])) \
                / (len(game_log[user_id][0]) + len(game_log[user_id][1]) + len(game_log[user_id][2]))
        waiting_list.append((user_rate * user_info[user['id']], user['id']))
    waiting_list.sort()

    for t in range(len(waiting_list) // 2):
        pairs.append([waiting_list[2*t][1], waiting_list[2*t+1][1]])

    return pairs

# Rate
# match user whose winrate + long loserate (over 10 min) is higher first
def match_rate4(waiting_line, user_info, game_log):
    # result of strategy
    pairs = []

    # get user score
    waiting_list = []
    for user in waiting_line:
        user_id = user['id']
        if (len(game_log[user_id][0]) + len(game_log[user_id][1]) + len(game_log[user_id][2])) == 0:
            user_rate = 50
        else:
            user_rate = (len(game_log[user_id][0]) + len(game_log[user_id][1])) \
                / (len(game_log[user_id][0]) + len(game_log[user_id][1]) + len(game_log[user_id][2]))
        waiting_list.append((-user_rate, user['id']))
    waiting_list.sort()

    for t in range(len(waiting_list) // 2):
        pairs.append([waiting_list[2*t][1], waiting_list[2*t+1][1]])

    return pairs

# Rate
# match users that similar user_rate
def match_rate5(waiting_line, user_info, game_log):
    # result of strategy
    pairs = []

    # get user score
    waiting_list = []
    for user in waiting_line:
        user_id = user['id']
        if (len(game_log[user_id][0]) + len(game_log[user_id][1]) + len(game_log[user_id][2])) == 0:
            user_rate = 50
        else:
            user_rate = (len(game_log[user_id][0]) + len(game_log[user_id][1])) \
                / (len(game_log[user_id][0]) + len(game_log[user_id][1]) + len(game_log[user_id][2]))
        waiting_list.append((user_rate, user['id']))
    waiting_list.sort()
    waiting_q = deque(waiting_list)

    tmp = deque([])
    while waiting_q:
        t = waiting_q.popleft()
        if t[1] > 0.1:
            tmp.append(t)
            if len(tmp) == 2:
                pairs.append([tmp[0][1], tmp[1][1]])
                tmp.clear()

    return pairs

############################################################
### Scenario 2 - Scoring (Abuser considered)
# Adjust constant score
# Longer the time means smaller the real score difference
# If 3 <= time <= 10, multiply score 0.2
# Scoring : |50 - (taken time)|
def score2_const(game_result, user_info):
    # result of score adjusting
    commands = []

    # game result parsing
    for game in game_result:
        winner, loser, taken_time = game['win'], game['lose'], game['taken']
        if taken_time in (3, 11):
            diff = (50 - taken_time) * 0
        else:
            diff = (50 - taken_time)

        win_command = {}
        win_command['id'] = winner
        win_command['grade'] = min(9999, user_info[winner] + diff)
        lose_command = {}
        lose_command['id'] = loser
        lose_command['grade'] = max(0, user_info[loser] - diff)

        commands.append(win_command)
        commands.append(lose_command)

    return commands

# Adjust constant score
# Longer the time means smaller the real score difference
# If 3 <= time <= 10 and loser's grade > winner's grade, multiply score 0.2
# Scoring : |50 - (taken time)|
def score2_const2(game_result, user_info):
    # result of score adjusting
    commands = []

    # game result parsing
    for game in game_result:
        winner, loser, taken_time = game['win'], game['lose'], game['taken']
        if taken_time in (3, 11) and user_info[loser] > user_info[winner]:
            diff = (50 - taken_time) * 0.2
        else:
            diff = (50 - taken_time)

        win_command = {}
        win_command['id'] = winner
        win_command['grade'] = min(9999, user_info[winner] + diff)
        lose_command = {}
        lose_command['id'] = loser
        lose_command['grade'] = max(0, user_info[loser] - diff)

        commands.append(win_command)
        commands.append(lose_command)

    return commands