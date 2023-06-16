# 프로그래머스 # 원하는 문자열 찾기

import re
def solution(myString, pat):
    if re.search(pat.lower(), myString.lower()):
        return 1
    return 0
