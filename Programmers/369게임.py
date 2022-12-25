# 프로그래머스 # 369게임

import re
def solution(order):
    return len(re.findall('[369]', str(order)))
