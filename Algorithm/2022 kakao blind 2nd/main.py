from scenario import *

############################################################
# base url and x_auth_token
base_url = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
x_auth_token = 'cebfedf449549f3948fc83119d93aca6'

# Accuracy 1 : | (real grade) - (predict grade) |
# Accuracy 2 : | (user A grade) - (user B grade) | at matching
# Efficiency : | R - waiting time |

### Scenario 1
# Matching      | Scoring       | Accuracy1 | Accuracy2 | Effi      | Total
# FIFO          | const         | 66.889	| 48.716	| 99.9	    | 218.65
# score         | const         | 60.0      | 52.2122   | 99.8742   | 214.554
# FIFO          | time          | 66.8889   | 48.716    | 99.8997   | 218.6456
# score2        | const         | 58.8889   | 61.3805   | 46.4722   | 181.5011 (SCORE_TH = 50)
# score2        | const         | 59.1111   | 56.4227   | 91.1462   | 211.5576 (SCORE_TH = 80)
# score2        | const         | 69.5556   | 64.3415   | 94.27     | 236.0924 (SCORE_TH = 100)
# score2        | const         | 54.4444   | 56.395    | 65.4902   | 185.3995 (SCORE_TH = 120)
# score_time    | const         | 58.6667   | 62.5333   | 99.8634   | 225.3307 (SCORE_TH = 100, TIME_TH = 10)
# score_time    | const         | 58.6667   | 62.5333   | 99.8634   | 225.3307 (SCORE_TH = 100, TIME_TH = 13)
# score2        | const2        | 61.1111   | 58.5653   | 96.9029   | 221.134  (SCORE_TH = 100, CONST_TIME = 45)
# score2        | const2        | 70.0      | 56.1316   | 91.9531   | 224.9205 (SCORE_TH = 100, CONST_TIME = 55)
# score2        | const3        | 57.7778   | 57.2179   | 56.6802   | 183.339  (SCORE_TH = 100)
# score2        | const3        | 63.5556   | 57.3965   | 96.0317   | 221.9679 (SCORE_TH = 150)
# score2        | const3        | 54.0      | 56.6513   | 99.0625   | 212.0315 (SCORE_TH = 200)
# scenario_1(base_url, x_auth_token)

### Scenario 2
# Matching      | Scoring       | Accuracy1 | Accuracy2 | Effi      | Total
# FIFO          | const         | 39.25	    | 54.147    | 99.877	| 191.98
# score         | const         | 28.3005   | 62.8756   | 99.8749   | 189.3112
# score2        | const         | 29.1323   | 63.2269   | 96,6085   | 188.1179 (SCORE_TH = 100)
# score_time    | const         | 29.9368   | 62.9415   | 99.8775   | 191.356  (SCORE_TH = 100, TIME_TH = 10)
# ABUSING CONSIDERED =======================================================
# FIFO          | 2_const (0.2) | 39.0136   | 54.1472   | 99.8766   | 191.6942
# FIFO          | 2_const (0)   | 39.1607   | 54.1472   | 99.8766   | 191.8708
# score         | 2_const (0.2) | 27.6802   | 62.3939   | 99.8749   | 187.9889
# score         | 2_const2 (0.2)| 28.6565   | 62.7599   | 99.3728   | 189.198
# rate          | const         | 40.5602   | 54.219    | 99.874    | 193.6343
# rate2         | const         | 27.5195   | 63.0633   | 96.4079   | 185.8257
# rate3         | const         | 28.664    | 63.6929   | 99.8743   | 190.7276
# rate4         | const         | 39.8652   | 54.6815   | 99.8764   | 193.3571
# rate5         | const         | 
scenario_2(base_url, x_auth_token)