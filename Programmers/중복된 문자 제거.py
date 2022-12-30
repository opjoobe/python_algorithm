# 프로그래머스 # 중복된 문자 제거

from collections import defaultdict
def solution(my_string):
    is_repeated = defaultdict(int)
    answer = ''
    for letter in my_string:
        if is_repeated[letter] == 1: continue
        answer += letter
        is_repeated[letter] = 1
    return answer