# 프로그래머스 # 둘만의 암호

def solution(s, skip, index):
    not_skip = [letter for letter in 'abcdefghijklmnopqrstuvwxyz' if letter not in skip]
    idx_dict = {letter:idx for idx, letter in enumerate(not_skip)}
    n = len(not_skip)
    cache = dict()
    answer = ''
    for letter in s:
        if letter not in cache:
            cache[letter] = not_skip[(idx_dict[letter] + index) % n]
        answer += cache[letter]
    return answer