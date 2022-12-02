# 프로그래머스 # 문자열 나누기

def solution(s):
    answer = 0
    x, x_cnt = '', 1
    for c in s:
        if not x:
            x, x_cnt = c, 1
            x_cnt = 1
            continue
        x_cnt = x_cnt + 1 if c == x else x_cnt - 1
        if x_cnt == 0:
            answer += 1
            x = ''
    return answer if not x else answer + 1