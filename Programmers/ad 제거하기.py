# 프로그래머스 # ad 제거하기

import re
def solution(strArr):
    p = r'ad'
    answer = [strng for strng in strArr if not re.search(p, strng)]
    return answer
