# 프로그래머스 # 대충 만든 자판

from collections import defaultdict
def solution(keymap, targets):
    answer = []
    min_press = defaultdict(int)
    for k in keymap:
        for cnt, letter in enumerate(k,1):
            if min_press[letter] != 0 and min_press[letter] <= cnt:
                continue
            min_press[letter] = cnt
    for target in targets:
        now = 0
        for letter in target:
            if min_press[letter] == 0:
                now = -1
                break
            now += min_press[letter]
        answer.append(now)
    return answer
