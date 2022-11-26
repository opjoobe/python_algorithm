# 프로그래머스 # k진수에서 소수 개수 구하기

import re
def solution(n, k):
    k_number = ''
    if k == 10:
        k_number = str(n)
    else:
        while n:
            n, rest = divmod(n, k)
            k_number += str(rest)
        k_number = k_number[::-1]
    candidates = list(map(int, re.findall('[123456789]+', k_number)))
    answer = 0
    for candidate in candidates:
        if candidate == 1: continue
        flag = True
        for num in range(2, int(candidate ** 0.5) + 1):
            if candidate % num == 0:
                flag = False
                break
        if flag:
            answer += 1
    return answer