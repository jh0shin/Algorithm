############################################################
### scenario.py
# Scenarios for each problem
# format : [{"truck_id": 0, "command": [2, 5, 4, 1, 6]}, ... ]
# ==========================================================
# scenario_1(base_url, x_auth_token)
# scenario_2(base_url, x_auth_token)

from kakao_parser import *
from strategy import *

############################################################
### Problem 1
def scenario_1(base_url, x_auth_token):
    # Get auth_key
    pkey = api_start(base_url, x_auth_token, 1)

    while True:
        ### Get bike rental center information
        raw_location = api_locations(base_url, pkey)
        bike_info = [0 for _ in range(5*5)]
        for info in raw_location:
            bike_info[info['id']] = info['located_bikes_count']
        # DEBUG
        # for b in bike_info: print(b)

        ### Get truck information
        raw_truck = api_trucks(base_url, pkey)
        truck_info = [dict() for _ in range(5*5)]
        for info in raw_truck:
            truck_info[info['location_id']][info['id']] = info['loaded_bikes_count']
        # DEBUG
        # for t in truck_info: print(t)

        ### Simulate
        commands = strategy_1_1(bike_info, truck_info)
        status, time, frcnt, dist = api_simulate(base_url, pkey, commands)
        if time % 60 == 0:
            print(f"{time} passed")
        # DEBUG 
        # print(status, time, frcnt, dist)

        # End simulation if status is not ready
        if status != 'ready': break

    score = api_score(base_url, pkey)
    print(f"Scenario 1 score : {score}")    

############################################################
### Problem 2
def scenario_2(base_url, x_auth_token):
    # Get auth_key
    pkey = api_start(base_url, x_auth_token, 2)

    while True:
        ### Get bike rental center information
        raw_location = api_locations(base_url, pkey)
        bike_info = [0 for _ in range(60*60)]
        for info in raw_location:
            bike_info[info['id']] = info['located_bikes_count']
        # DEBUG
        # for b in bike_info: print(b)

        ### Get truck information
        raw_truck = api_trucks(base_url, pkey)
        truck_info = [dict() for _ in range(60*60)]
        for info in raw_truck:
            truck_info[info['location_id']][info['id']] = info['loaded_bikes_count']
        # DEBUG
        # for t in truck_info: print(t)

        ### Simulate
        commands = strategy_1_1(bike_info, truck_info)
        status, time, frcnt, dist = api_simulate(base_url, pkey, commands)
        if time % 60 == 0:
            print(f"{time} passed")
        # DEBUG 
        # print(status, time, frcnt, dist)

        # End simulation if status is not ready
        if status != 'ready': break

    score = api_score(base_url, pkey)
    print(f"Scenario 2 score : {score}")    
